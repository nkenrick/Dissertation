import pygame, sys
from mazeGenerator import *
from agent import *
pygame.init()

'''
Original proof of concept program. Allows a user to move agent
around in a maze.
'''

#Exception for collisions
class MyError(Exception):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return repr(self.message)

#Make wall sprite to allow collision
class Wall(pygame.sprite.Sprite): 	
	def __init__(self, x, y, surface): 
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.Surface([30, 30]) 
		self.image.fill((0, 0, 0)) 
		self.rect = self.image.get_rect() 
		self.rect.x = x 
		self.rect.y = y 
		pygame.draw.rect(surface, (0, 0, 0), self.rect) 

#Create sprite group
agents = pygame.sprite.Group()
walls = pygame.sprite.Group()

#Checks if maze exists, if not makes one
#Returns created or read mazeObject
def getObject(name, size):	
	try:
		mazeSize = open(name + ".txt", "r")
		mazeObject = Maze(size[0], size[1], mazeSize.read())
		mazeSize.close()
	except FileNotFoundError:
		mazeSize = open(name + ".txt", "a")
		mazeObject = Maze(size[0], size[1], [])
		mazeSize.write(str(mazeObject.maze))
		mazeSize.close()

	return mazeObject

#set maze size, defult is large
small = [10, 10]
medium = [20, 20]
size = [30, 30]

if len(sys.argv) > 1:
	if sys.argv[1] == 'small':
		size = small
	elif sys.argv[1] == 'medium':
		size = medium
	elif sys.argv[1] == 'testMaze':
		size = small
	mazeObject = getObject(sys.argv[1], size)
else:
	mazeObject = getObject("large", size)

cubeSize = 30
mHeight, mWidth = size[0], size[1]
sWidth, sHeight = (mHeight * cubeSize), (mWidth * cubeSize)
screen = pygame.display.set_mode((sWidth, sHeight))

#Draw maze 
def drawMaze(setup):
	xPos = 0
	yPos = 0
	for i in range(0, mWidth):
		xPos = 0
		for j in range(0, mHeight):
			
			if mazeObject.maze[i][j] == 'w':
				if setup: # Initial drawing sets collision sprites
					walls.add(Wall(xPos, yPos, screen))
				else:
					pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
			else:
				pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(xPos, yPos, cubeSize, cubeSize))
			xPos += 30
		yPos += 30


startX, startY = int(size[0]/2)*30,  int(size[1]/2)*30
agent = Agent(startX, startY)
agents.add(agent)

drawMaze(True)
count = 0

mazeObject.printMaze()
running = True

#Main game loop
while running:

	pygame.time.delay(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	currentPos = [agent.rect.x, agent.rect.y]
	
	try:
		agent.move()
		if pygame.sprite.groupcollide(agents, walls, False, False):
			raise MyError("That is a wall")
	except MyError as error:
		agent.handleCollsion(currentPos)

	drawMaze(False)		
	agent.draw(screen)

	pygame.display.update()














