#Maze Generator 
import random
from ast import literal_eval
from colorama import init, Fore 
from getChildren import get_children
init()

'''
Randomly generate a maze in the form of a 2D array 
'''

#create maze object
class Maze():
	def __init__(self, width, height, maze):
		self.width = width
		self.height = height
		if maze == []:
			self.maze = self.generate(width, height)
		else:
			if isinstance(maze,str):
				self.maze = literal_eval(maze)
			else:
				self.maze = maze
			

	def get_maze(self):
		return self.maze
	
	def get_cells(self):
		cells = []
		for i in range(len(self.maze)):
			for j in range(len(self.maze)):
				if self.maze[i][j] == 'c':
					cells.append((i, j))
		return cells
	
	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def printMaze(self):
		maze = self.maze
		if maze == []:
			print ("a")
		for i in range(0, len(maze)):
			for j in range(0, len(maze[0])):
				if maze[i][j] == 'u':
					print(Fore.WHITE, f'{maze[i][j]}', end="")
				elif maze[i][j] == 'c':
					print(Fore.GREEN, f'{maze[i][j]}', end="")
				else:
					print(Fore.RED, f'{maze[i][j]}', end="")
			print('\n')

	def fillMaze(self, width, height):
		maze = []
		for i in range(0, height):
			line = []
			for j in range(0, width):
				line.append('u')
			maze.append(line)
	
		return maze


	def surroundingCells(self, maze, randWall):
		sCells = 0
		if (maze[randWall[0]-1][randWall[1]] == 'c'):
			sCells += 1

		if (maze[randWall[0]+1][randWall[1]] == 'c'):
			sCells += 1

		if (maze[randWall[0]][randWall[1]-1] == 'c'):
			sCells += 1

		if (maze[randWall[0]][randWall[1]+1] == 'c'):
			sCells += 1

		return sCells

	def generate(self, width, height):
		startingHeight = int(height / 2)
		startingWidth = int(width/2)

		maze = self.fillMaze(width, height)

		maze[startingHeight][startingWidth] = 'c'
		walls = []
		walls.append([startingHeight-1, startingWidth])
		walls.append([startingHeight, startingWidth-1])
		walls.append([startingHeight, startingWidth+1])
		walls.append([startingHeight+1, startingWidth])

		def up(maze, randWall, walls):
			if (randWall[0] != 0):
				if (maze[randWall[0]-1][randWall[1]] != 'c'):
					maze[randWall[0]-1][randWall[1]] = 'w'
				if ([randWall[0]-1, randWall[1]] not in walls):
					walls.append([randWall[0]-1, randWall[1]])

		def bottom(maze, randWall, walls):
			if (randWall[0] != height-1):
				if (maze[randWall[0]+1][randWall[1]] != 'c'):
					maze[randWall[0]+1][randWall[1]] = 'w'
				if ([randWall[0]+1, randWall[1]] not in walls):
					walls.append([randWall[0]+1, randWall[1]])

		def left(maze, randWall, walls):
			if (randWall[1] != 0):
				if (maze[randWall[0]][randWall[1]-1] != 'c'):
					maze[randWall[0]][randWall[1]-1] = 'w'
				if ([randWall[0], randWall[1]-1] not in walls):
					walls.append([randWall[0], randWall[1]-1])

		def right(maze, randWall, walls):
			if (randWall[0] != width-1):
				if (maze[randWall[0]][randWall[1]+1] != 'c'):
					maze[randWall[0]][randWall[1]+1] = 'w'
				if ([randWall[0], randWall[1]+1] not in walls):
					walls.append([randWall[0], randWall[1]+1])

		def deleteFromList(walls, randWall):
			for wall in walls:
				if(wall[0] == randWall[0] and wall[1] == randWall[1]):
					walls.remove(wall)

		while walls:
			randWall = walls[int(random.random()*len(walls))-1] #While there are walls, pick random wall
			#Left
			if (randWall[1] != 0):
				if maze[randWall[0]][randWall[1]-1] == 'u' and maze[randWall[0]][randWall[1]+1] == 'c':
					sCells = self.surroundingCells(maze, randWall)
					if sCells < 2:
						maze[randWall[0]][randWall[1]] = 'c' #New path

						up(maze, randWall, walls)
						bottom(maze, randWall, walls)
						left(maze, randWall, walls)
					
					deleteFromList(walls, randWall)


			#Up
			if (randWall[0] != 0):
				if maze[randWall[0]-1][randWall[1]] == 'u' and maze[randWall[0]+1][randWall[1]] == 'c':
					sCells = self.surroundingCells(maze, randWall)
					if sCells < 2:
						maze[randWall[0]][randWall[1]] = 'c' #New path
						
						up(maze, randWall, walls)
						right(maze, randWall, walls)
						left(maze, randWall, walls)
					
					deleteFromList(walls, randWall)

			#Bottom
			if (randWall[0] != height - 1):
				if maze[randWall[0]+1][randWall[1]] == 'u' and maze[randWall[0]-1][randWall[1]] == 'c':
					sCells = self.surroundingCells(maze, randWall)

					if sCells < 2:
						maze[randWall[0]][randWall[1]] = 'c' #New path
					
						bottom(maze, randWall, walls)
						left(maze, randWall, walls)
						right(maze, randWall, walls)

					deleteFromList(walls, randWall)
			
			#Right
			if (randWall[1] != width - 1):
				if maze[randWall[0]][randWall[1]+1] == 'u' and maze[randWall[0]][randWall[1]-1] == 'c':
					sCells = self.surroundingCells(maze, randWall)

					if sCells < 2:
						maze[randWall[0]][randWall[1]] = 'c' #New path
						
						left(maze, randWall, walls)
						right(maze, randWall, walls)
						up(maze, randWall, walls)
						bottom(maze, randWall, walls)

					deleteFromList(walls, randWall)
			
			deleteFromList(walls, randWall)

		for i in range(0, height):
			for j in range(0, width):
				if (maze[i][j] == 'u'):
					maze[i][j] = 'w'
		
		count = 0
		length = len(maze[0])
		
		def upDown(x, y):
			if maze[x+1][y] == 'c' and maze[x-1][y] == 'c':
				return 'c'

			elif maze[x+1][y] == 'w' and maze[x-1][y] == 'w':
				return 'w'

			return False

		def leftRight(x, y):
			if maze[x][y+1] == 'c' and maze[x][y-1] == 'c':
				return 'c'

			elif maze[x][y+1] == 'w' and maze[x][y-1] == 'w':
				return 'w'

			return False
	

		# Create free outer ring - step 1 move all walls in outer ring inwards
		for i in range(1, width-1):
			if maze[1][i] == 'w':
				if maze[2][i] == 'c':
					maze[2][i] = 'w'
				maze[1][i] ='c'

			if maze[width-2][i] == 'w':
				if maze[width-3][i] == 'c':
					maze[width-3][i] = 'w'
				maze[width- 2][i] ='c'

			if maze[i][1] == 'w':
				if maze[i][2] == 'c':
					maze[i][2] = 'w'
				maze[i][1] ='c'
				
			if maze[i][height-2] == 'w':
				if maze[i][width-3] == 'c':
					maze[i][width-3] = 'w'
				maze[i][width-2] ='c'

		#step 2 - if new wall cause diagonally agecent cells,  turn them into walls
		for i in range(2, width-2):
			if maze[2][i] == 'c':
				if maze[3][i+1] == 'c' or maze[3][i-1] == 'c':
					maze[2][i] = 'w'

			if maze[width-3][i] == 'c':
				if maze[width-4][i+1] == 'c' or maze[width-4][i-1] == 'c':
					maze[width-3][i] ='w'

			if maze[i][2] == 'c':
				if maze[i+1][3] == 'c' or maze[i-1][3] == 'c':
					maze[i][2] = 'w'

			if maze[i][width-3] == 'c':
				if maze[i+1][width-4] == 'c' or maze[i-1][width-4] == 'c':
					maze[i][width-3] ='w'


		rounds = 0
		while count != length**4 and rounds < length**3:
			rounds += 1
			x = random.randint(1, (length-2))
			y = random.randint(1, (length-2))
			
			if maze[x][y] == 'w':
				if (upDown(x, y) == 'c' and leftRight(x, y) == 'w') or (upDown(x, y) == 'w' and leftRight(x, y) == 'c'): 
					maze[x][y] = 'c'
					count += 1

		# Make sure edges are completely clear and there are no dead ends 
		x = 1
		while x>0:
			x = 0
			for i in range(1, width-2):
				for j in range(1, width-2):
					if maze[i][j] == 'c' and len(get_children(maze, (i, j))) == 1:
						maze[i][j] = 'w'
						x+=1
					if i == 1 or i == width-2 or j == width-2 or j == 1:
						maze[i][j] = 'c'

		return maze
