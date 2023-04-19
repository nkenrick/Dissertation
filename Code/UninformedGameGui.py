from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame, sys
from mazeGenerator import *
from makeGraph import *
from BreadthFirstSearch import BFS
from DepthFirstSearch import DFS
from DLDFS import DLDFS
from UniformCostSearch import UCS
import time
from heuristic import *
from graphRep import *
from informedAgent import*
from EnemyAgent import *
from PlayerAgent import *
from ProblemSolvingAgent import ProblemSolvingAgent

'''
	Class for displaying uninformed searches in deliverable
'''



class Game():
	def __init__(self, visualise, search, maze_size, start_pos, goal_pos, maze):
		self.game_state = True
		self.search = search
		if maze_size == 'Small':
			self.maze_size = 12
		elif maze_size == 'Large':
			self.maze_size = 30
		else:
			self.maze_size = 20
		if maze != None and len(maze[0]) == self.maze_size:
			self.maze_object = Maze(self.maze_size, self.maze_size, maze)
		else:
			self.maze_object = Maze(self.maze_size, self.maze_size, [])
		self.start_pos = start_pos
		self.goal_pos = goal_pos
		self.visualise = visualise


	def get_game_state(self):
		return self.game_state

	def finished(self):
		self.game_state = False


	def draw(self):
		cubeSize = 30
		mHeight, mWidth = self.maze_size, self.maze_size
		sWidth, sHeight = (mHeight * cubeSize), (mWidth * cubeSize)
		screen = pygame.display.set_mode((sWidth, sHeight))
		maze = self.maze_object.get_maze()
		#Draw maze 
		def drawMaze(visited):
			xPos = 0
			yPos = 0
			for i in range(0, mHeight):
				xPos = 0
				for j in range(0, mWidth):
					if goal != None and i == goal[0] and j == goal[1]:
						pygame.draw.rect(screen, (0, 141, 97), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
						pygame.draw.circle(screen, (255, 0, 0),[xPos+15, yPos+15], 12, 0)
					elif maze[i][j] == 'w':
						pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
					elif (i, j) in visited:
						pygame.draw.rect(screen, (141, 0, 44), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
					else:
						pygame.draw.rect(screen, (0, 141, 97), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
					xPos += 30
				yPos += 30


		# Start Position
		if self.start_pos == 'Centre':
			startX, startY = int(self.maze_size/2),  int(self.maze_size/2)
			start_coord = (startX, startY)
		elif self.start_pos == 'Corner':
			positions = [(mHeight-2, mHeight-2), (1, mHeight-2), (mHeight-2, 1), (1, 1)]
			x = random.randint(0, 3)
			start_coord = positions[x]
		else:
			x = random.randint(1, mHeight-2)
			y = random.randint(1, mHeight-2)
			start_coord = (x, y)
			if maze[x][y] == 'w':
				xdir = 1
				ydir = 1
				move = 0
				while maze[x][y] == 'w': # Approx corner, may be slightly off 
					if x >= mHeight-2: # make sure not to move position off of screen
						xdir = -1
					if y >= mHeight -2:
						ydir = -1

					if move == 0:
						y = y + ydir
					elif move ==1:
						x =x +xdir
					else:
						y = y+ydir
						x = x+xdir
					move = (move + 1)%3
					start_coord = (x, y)
		visited = [start_coord]
		
		# Goal position
		if self.goal_pos == 'Centre':
			goal =  (int(self.maze_size/2),  int(self.maze_size/2))
		elif self.goal_pos == 'Corner':
			goals = [(mHeight-2, mHeight-2), (1, mHeight-2), (mHeight-2, 1), (1, 1)]
			x = random.randint(0, 3)
			goal = goals[x]
		else:
			x = random.randint(1, mHeight-2)
			y = random.randint(1, mHeight-2)
			goal = (x, y)
			if maze[x][y] == 'w':
				xdir = 1
				ydir = 1
				move = 0
				while maze[x][y] == 'w' or (x, y) == start_coord: # Approx corner, may be slightly off 
					if x >= mHeight-2: # make sur enot to move goal off of screen
						xdir = -1
					if y >= mHeight -2:
						ydir = -1

					if move == 0:
						y = y + ydir
					elif move ==1:
						x =x +xdir
					else:
						y = y+ydir
						x = x+xdir
					move = (move + 1)%3
					goal = (x, y)

		agent = ProblemSolvingAgent(start_coord[0], start_coord[1], self.search, self.maze_object, goal, ((255, 251, 0)))
		
		#Main game loop
		running = True
		start = time.time()
		while running:
			cont = self.get_game_state()
			if cont:
				pygame.time.delay(50)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = False
				currentPos = [agent.rect.x, agent.rect.y]

				visited.append(agent.move())

				drawMaze(visited)
				
				if visited[-1] == True:
					self.finished()

				agent.draw(screen) 
				pygame.display.update()

			else:
				time_taken = time.time() - start
				
				self.visualise.end_game((visited[-1] == True), time_taken, len(visited), self.maze_object.get_maze())
				break
		
				











