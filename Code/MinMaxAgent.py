from Agent import Agent
import math
import numpy as np
from graphRep import *
from travereseAll import *
'''
Class for agent that uses Minmax algorithm
'''
class MinMaxAgent(Agent):
	def __init__(self, x, y, search, mazeObject, goal, colour, game):
		super().__init__(x, y, search, mazeObject, colour)
		self.game = game
		self.goal = []
		if goal == 'all': ## Get route to traverse entire maze 
			self.goal = mazeObject.get_cells()
		elif not isinstance(goal, list): # Allows for multiple goals
			self.goal = [goal] 
		else:
			self.goal = goal
		self.graph = Graph(mazeObject, (int(mazeObject.get_width()/2), int(mazeObject.get_height()/2)), self.goal)


		# Multiple agents
		self.villans = []
		self.reaval = False
		self.visited = [(x, y)]
		self.route =[]
		self.check = False
		self.depth = 2


	def move(self):

		if self.route == None:
			self.route = []

		if self.goal == []:
			return True

		enemy_actions = []
		for enemy in self.villans:
			if self.get_pos() == enemy.get_pos():
				self.game.finished()
			actions = get_children(self.mazeObject.get_maze(), enemy.get_pos())
			actions.append(enemy.get_pos())
			enemy_actions = enemy_actions + actions

		if len(self.visited) <= 2:
			self.route.append(self.max_p(self.get_pos(), 0, enemy_actions, []))
		else:
			self.route.append(self.max_p(self.get_pos(), 0, enemy_actions, [self.visited[-2]]))


		if self.visited == []:
			self.route = [self.get_pos()]
		if self.route != []:
			next_step = self.route[0]
			self.route.remove(next_step)
			if next_step in self.goal:
				self.goal.remove(next_step)
			self.rect.x = next_step[1] * 30
			self.rect.y = next_step[0] * 30
			self.visited.append(self.get_pos())
			return next_step

	def max_p(self, pos, depth, enemy_actions, past):
		depth+=1
		actions = get_children(self.mazeObject.get_maze(), pos)
		max_option = -math.inf
		choice = None
		if len(self.visited) >= 16:
			self.check_deadlock()

		past.append(pos)


		if self.check:
			return self.run(pos, self.closest(pos))

		for action in actions:
			score = self.min_e(action, depth, enemy_actions, past, max_option)
			if score > max_option or choice == None:
				max_option = score
				choice = action

		if depth == 1:
			return choice
		else:
			return max_option
	
	def min_e(self, player_action, depth, enemy_actions,past, cur_max):
		min = math.inf
		for enemy_move in enemy_actions:
			actions = get_children(self.mazeObject.get_maze(), enemy_move)
			actions.append(enemy_move)
			for action in enemy_actions:
				score = self.evaluationFunction(player_action, action,past)
				if depth < self.depth:
					score = score +self.max_p(player_action, depth, actions,copy(past))
				if score < min:
					min = score
				if depth == self.depth and score < cur_max: # Pruning 
					return score
		return min

	def evaluationFunction(self, state, enemy, past):
		''' Return score of state '''
		score = 0
		if state == enemy:
			score = -math.inf
		elif state in self.goal and state not in past:
			score = 1000
		elif score == 0:
			dist = self.best(state)
			score = 100/dist
		if state in past[-2:]:
			score -= 15
		return score


	def check_deadlock(self):	
		self.check =  all(item in self.visited[-8:] for item in self.visited[-16:][:8])
	
	def add_villan(self, villan):
		self.villans.append(villan)


	def run(self, pos, enemy_pos):
		''' Choose furthest node from enemy '''
		children = get_children(self.mazeObject.get_maze(), pos)
		for child in children:
			if len(get_children(self.mazeObject.get_maze(), child)) == 1:
				children.remove(child)
		choice = None
		dist = 0
		for child in children:
			new_dist = (abs(enemy_pos[0] - child[0]) + abs(enemy_pos[1] - child[1]))
			if  new_dist > dist:
				choice = child
				dist = new_dist
		return choice

	def closest(self, pos):
		''' Return closest enemy'''
		closest = None
		dist = math.inf
		for enemy in self.villans:
			new_dist = (abs(enemy.get_pos()[0] - pos[0]) + abs(enemy.get_pos()[1] - pos[1]))
			if new_dist < dist:
				dist = new_dist
				closest = enemy 
		return closest.get_pos()

	def best(self, pos):
		''' Return next best node '''
		goals = copy(self.goal)
		if pos in goals:
			goals.remove(pos)
		dist = math.inf 
		for i in range(0, len(goals)):
			new_dist =  (abs(goals[i][0] - pos[0]) + abs(goals[i][1] - pos[1]))
			if new_dist <= dist:
				dist = new_dist
		if dist == 0:
			dist = 1
		return dist