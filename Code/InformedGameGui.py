from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame, sys
from mazeGenerator import *
from makeGraph import *
import time
from heuristic import *
from informedSearch import Informed
from graphRep import *
from informedAgent import*
from EnemyAgent import *
from PlayerAgent import *
from MinMaxAgent import MinMaxAgent
from MinMaxEnemyAgent import MinMaxEnemyAgent
from ExpectimaxAgent import ExpectimaxAgent
from ExpectimaxEnemy import ExpectimaxEnemy

'''Game class for informed algorithms called by user interface'''

class IGame():
	def __init__(self, search, maze_size, visualise, maze, num_enemy=1):
		self.visualise = visualise
		self.game_state = True
		self.search = search
		self.num_enemy = num_enemy
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
					if maze[i][j] == 'w':
						pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
					elif (i, j) in visited:
						pygame.draw.rect(screen, (0, 141, 97), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
					else:
						pygame.draw.rect(screen, (0, 141, 97), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
						pygame.draw.circle(screen, (255, 255, 255),[xPos+15, yPos+15], 5, 0)
					xPos += 30
				yPos += 30

		
		startX, startY = int(self.maze_size/2),  int(self.maze_size/2)
		positions = [(mHeight-2, 1), (1, mHeight-2),  (1, 1), (mHeight-2, mHeight-2)]
		colours = [(195, 0, 241), (241, 0, 42), (241, 74, 0)]
		start_coord = (startX, startY)
		visited = [start_coord]
		game = self
		search = Informed('m', 'path', 'A*') #Chosen search to show 
		if self.search == 'MinMax':
			agent = MinMaxAgent(start_coord[0], start_coord[1], search, self.maze_object, 'all', (255, 251, 0), game)
		elif self.search == 'Expectimax':
			agent = ExpectimaxAgent(start_coord[0], start_coord[1], search, self.maze_object, 'all', (255, 251, 0), game)
		else:
			agent = PlayerAgent(start_coord[0], start_coord[1], search, self.maze_object, 'all', (255, 251, 0), game)
		
		radius = [12, 4, 1]
		enemies = []
		for i in range(0, self.num_enemy):
			new_enemy = ExpectimaxEnemy(positions[i][0], positions[i][1], search, self.maze_object, agent, colours[i], game, radius[i])
		
			enemies.append(new_enemy)

		for enemy in enemies:
			agent.add_villan(enemy)
				
		#Main game loop
		var = 0
		start = time.time()
		running = True
		while running:
			cont = game.get_game_state()
			if cont:
				pygame.time.delay(80)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = False

				visited.append(agent.move())
				if var == 2:
					for enemy in enemies:
						enemy.move()
					var = 0
				drawMaze(visited)
				
				if visited[-1] == True:
					game.finished()
				var +=1
				for enemy in enemies:
					enemy.draw(screen)
				agent.draw(screen) 

				pygame.display.update()
			else:
				time_taken = time.time() - start
				self.visualise.end_game((visited[-1] == True), time_taken, len(visited), self.maze_object.get_maze())
				break
				











