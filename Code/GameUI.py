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
from informedSearch import Informed
from graphRep import *
from informedAgent import*
from EnemyAgent import *
from PlayerAgent import *
from ProblemSolvingAgent import ProblemSolvingAgent
from MinMaxAgent import MinMaxAgent
from MinMaxEnemyAgent import MinMaxEnemyAgent
from ExpectimaxAgent import ExpectimaxAgent
from ExpectimaxEnemy import ExpectimaxEnemy
pygame.init()

''' Class used for testing algorithms during development'''

class Game():
	def __init__(self):
		self.game_state = True

	def get_game_state(self):
		return self.game_state

	def finished(self):
		self.game_state = False

#Checks if maze exists, if not makes one
#Returns created or read mazeObject
def get_object(name, size):	
	try:
		mazeSize = open(name + ".txt", "r")
		mazeObject = Maze(size[0], size[1], mazeSize.read())
		mazeSize.close()
	except FileNotFoundError:
		mazeSize = open("bug.txt", "w")
		mazeObject = Maze(size[0], size[1], [])
		mazeSize.write(str(mazeObject.get_maze()))
		mazeSize.close()

	return mazeObject

#set maze size, defult is large
small = [12, 12]
medium = [20, 20]
large = [30, 30]
size = medium
if len(sys.argv) > 1:
	if sys.argv[1] == 'test':
		size = size
	elif sys.argv[1] == 'bug':
		size = size
	mazeObject = get_object(sys.argv[1], size)
else:
	#mazeObject = get_object("large", size)
	mazeObject = get_object('test', size)

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
				pygame.draw.circle(screen, (255, 255, 255),[xPos+15, yPos+15], 5, 0)
			xPos += 30
		yPos += 30

startX, startY = int(size[0]/2),  int(size[1]/2)
start_coord = (startX, startY)
visited = [start_coord]
running = True

'All goals used for testing'
#goal = (1, 1)
#goal = (5, 5)
#goal = (7, 7)
#goal = (int(size[0]/2), int(size[1]/2))
goal = None

#find corners
corners = [(1, mHeight-2), (1, 1), (mHeight-2, 1), (mHeight-2, mHeight-2)]
for i in range (0, len(corners)):
	x = corners[i][0]
	y = corners[i][1]
	if maze[x][y] == 'w':
		while  maze[x][y] == 'w':
			y = y - 1
		corners[i] = (x, y)



start = time.time()
game = Game()
search = Informed('m', 'path', 'A*') #Chosen search to show 
agent = MinMaxAgent(start_coord[0], start_coord[1], search, mazeObject, 'all', (255, 251, 0), game)
enemy1 = ExpectimaxEnemy(1, 1, search, mazeObject, agent, (255, 0, 0), game, 12)
enemies = []
enemies.append(enemy1)

for enemy in enemies:
	agent.add_villan(enemy)

#Main game loop
var = 0
start = time.time()
while running:
	cont = game.get_game_state()
	if cont:
		pygame.time.delay(110)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		currentPos = [agent.rect.x, agent.rect.y]

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
		if visited[-1] == True:
			print('Winner!')
		else:
			print('Game Over!')
		print('Steps:', len(visited))
		print(time.time() - start)
		break
		












