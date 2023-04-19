from Agent import Agent
import math
import numpy as np
from graphRep import *
from travereseAll import *
import random
'''
 	Code for QLearning agent that navigates maze to find goal using informed search algorithm
'''
class QLearningAgent(Agent):
	def __init__(self, x, y, search, mazeObject, goal, colour):
		super().__init__(x, y, search, mazeObject, colour)
		self.goal = goal
		self.graph = Graph(mazeObject, (int(mazeObject.get_width()/2), int(mazeObject.get_height()/2)), self.mazeObject.get_cells())

		self.cells = mazeObject.get_cells()

		# Multiple agents
		self.villan = None
		self.route =[]
		self.startx = x
		self.starty = y
		self.visited = [(x, y)]

		self.q_table = {}

		# Initiate q-table
		for goal in self.cells:
			children = get_children(self.mazeObject.get_maze(), goal)
			actions = [-1, -1, -1, -1] # Left, Right, Up, Down
			if (goal[0] , goal[1]-1) not in children: # Left
				actions[0] = -math.inf
			if (goal[0] , goal[1]+1) not in children: # Right
				actions[1] = -math.inf
			if (goal[0]-1, goal[1]) not in children: # Up
				actions[2] = -math.inf
			if (goal[0]+1, goal[1]) not in children: # Down
				actions[3] = -math.inf
			self.q_table[goal] = actions

		self.e = 0.4 
		self.l_rate = 0.8 # Learning Rate 
		self.d_rate = 0.95 # Discount Rate 

	def get_Qtable(self):
		return self.q_table
	
	def set_epsilon(self, e):
		self.e = e

	def move(self):
		pos = self.get_pos()

		x = random.random()
		action = None
		actions = self.q_table[pos]

		if x > self.e: # Exploit
			dir = actions.index(max(actions))
			action = self.get_action(pos, dir)
		else: # Explore 
			action = -math.inf
			dir = -1
			while action == -math.inf:
				dir = random.randint(0, 3)
				choice = actions[dir]
				if choice != -math.inf:
					action = self.get_action(pos, dir)

		reward = self.evaluationFunction(action)
		actions[dir] = actions[dir] + self.l_rate*(reward + (self.d_rate*max(self.q_table[action])) - actions[dir])

		self.rect.x = action[1] * 30
		self.rect.y = action[0] * 30
		self.visited.append(action)
		return action

	def evaluationFunction(self, state):
		score = 0
		if state == self.goal:
			score = 10
		elif state in self.visited[-3:]:
			score = -1.5
		else:
			score = -1
		return score


	def add_villan(self, villan):
		self.villan = villan

	def get_action(self, state, direction):
		if direction == 0:
			return (state[0] , state[1]-1)
		elif direction == 1:
			return (state[0] , state[1]+1)
		elif direction == 2:
			return (state[0]-1 , state[1])
		else:
			return (state[0]+1 , state[1])
	
	def reset(self):
		self.e = self.e *0.99  # Get smaller
		self.rect.x = self.startx * 30
		self.rect.y = self.starty * 30
