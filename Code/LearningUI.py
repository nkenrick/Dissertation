from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame, sys
import math
from mazeGenerator import *
import time
from heuristic import *
from QLearningAgent import QLearningAgent
from ExpectimaxEnemy import ExpectimaxEnemy
from informedSearch import Informed
from PlayerAgent import PlayerAgent
from copy import copy



''' Class used for Qlearning Agent '''

class QGame():
	def __init__(self, visualise):
		self.game_state = True
		self.visualise = visualise

	def get_game_state(self):
		return self.game_state

	def finished(self):
		self.game_state = False

	#Checks if maze exists, if not makes one
	#Returns created or read mazeObject
	def get_object(name, size):	
		mazeSize = open(name, "r")
		mazeObject = Maze(size[0], size[1], mazeSize.read())
		mazeSize.close()

		return mazeObject

	def draw(self):
		size = [20, 20]
		# Maze used for this algorithm
		mazeArray  = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
					 ['w', 'c', 'w', 'c', 'w', 'w', 'w', 'c', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w'], 
					 ['w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'c', 'w', 'c', 'w', 'w', 'w', 'c', 'w'], 
					 ['w', 'c', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'w', 'c', 'w', 'w', 'w', 'w', 'w', 'c', 'c', 'w'], 
					 ['w', 'c', 'w', 'c', 'c', 'w', 'w', 'w', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'w', 'w', 'c', 'w'], 
					 ['w', 'c', 'w', 'w', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'w'], 
					 ['w', 'c', 'c', 'c', 'c', 'w', 'c', 'w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'w', 'c', 'w'], 
					 ['w', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'w', 'w'], 
					 ['w', 'w', 'w', 'w', 'w', 'c', 'w', 'c', 'w', 'w', 'c', 'w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], 
					 ['w', 'c', 'w', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'c', 'w'], 
					 ['w', 'c', 'c', 'c', 'w', 'c', 'w', 'w', 'w', 'w', 'c', 'c', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'w'], 
					 ['w', 'c', 'w', 'c', 'w', 'c', 'w', 'w', 'w', 'w', 'w', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'c', 'w'], 
					 ['w', 'c', 'w', 'w', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'w', 'c', 'w', 'w', 'w', 'c', 'c', 'w'], 
					 ['w', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'w', 'w'], 
					 ['w', 'w', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'w', 'c', 'w', 'c', 'w', 'w'], 
					 ['w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'], 
					 ['w', 'c', 'w', 'w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'c', 'w'], 
					 ['w', 'c', 'w', 'c', 'c', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'c', 'w', 'c', 'w'], 
					 ['w', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'w', 'c', 'w', 'w', 'c', 'w'], 
					 ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']]
		mazeObject = Maze(size[0], size[1], mazeArray)

		cubeSize = 30
		mHeight, mWidth = size[0], size[1]
		sWidth, sHeight = (mHeight * cubeSize), (mWidth * cubeSize)
		screen = pygame.display.set_mode((sWidth, sHeight))
		maze = mazeObject.get_maze()
		#Draw maze 
		def drawMaze(visited):
			xPos = 0
			yPos = 0
			for i in range(0, mHeight):
				xPos = 0
				for j in range(0, mWidth):
					if goal != None and i == goal[0] and j == goal[1]:
						pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
					elif maze[i][j] == 'w':
						pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
					elif (i, j) in visited:
						pygame.draw.rect(screen, (0, 141, 97), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
					else:
						pygame.draw.rect(screen, (0, 141, 97), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
					xPos += 30
				yPos += 30

		startX, startY = 1, 1
		start_coord = (startX, startY)
		visited = [start_coord]
		running = True

		start = time.time()
		game = QGame(self.visualise)

		goal = ((mWidth -2), (mHeight-2))

		search = Informed('e', 'path', 'A*') #Chosen search to show 
		agent = QLearningAgent(startX, startY, search, mazeObject,  goal, (255, 251, 0))

		goal_length = 0
		q_table = {}

		#Main game loop
		var = 0
		start = time.time()
		episode = 1
		fin = False
		while running:
			cont = game.get_game_state()
			

			if goal_length < 1 and episode <1000:
				if cont:
					currentPos = [agent.rect.x, agent.rect.y]
					visited.append(agent.move())
					
					if visited[-1] == goal:
						game.finished()

				else:
					if len(visited) == 34:
						goal_length += 1
					episode += 1
					visited = []
					agent.reset()
					game.game_state = True
			else:
				pygame.init()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = False
				if cont:
					agent.set_epsilon(0)
					pygame.time.delay(110)
					currentPos = [agent.rect.x, agent.rect.y]
					visited.append(agent.move())
					drawMaze(visited)
					
					if visited[-1] == goal:
						game.finished()

					agent.draw(screen) 
					pygame.display.update()
				else:
					self.visualise.end_game(True, None, len(visited), maze,  learning=episode)
					break












