from Agent import Agent
import numpy as np
from graphRep import *
from travereseAll import *
'''
Class for enemy MinMax agent. Goal is agent if within 10 steps, otherwise searches for agent by going to its furthest point.
'''
class MinMaxEnemyAgent(Agent):
	def __init__(self, x, y, search, mazeObject, target, colour, game, radius):
		super().__init__(x, y, search, mazeObject, colour)
		self.target = target
		self.cells = mazeObject.get_cells()
		self.graph = Graph(mazeObject, (int(mazeObject.get_width()/2), int(mazeObject.get_height()/2)), 'ALL')

		self.chase = False
		self.visited = []
		self.RADIUS = radius
		self.check = False
		self.game = game
		self.depth = 2
		self.enemies = []


	def move(self):
		if self.get_pos() == self.target.get_pos():
			self.game.finished()
		if self.route == None:
			self.route = []

		if len(self.visited) >= 8:
			self.check_deadlock()

		if self.check:
			self.route = [self.get_pos()] + self.route

		else:
			
			if np.linalg.norm(np.asarray(self.get_pos())-np.asarray(self.target.get_pos())) >self.RADIUS:
				self.chase = False 
			else:
				self.chase = True	
			
			if self.chase:
				self.route = []
				self.route.append(self.max_p(self.get_pos(), 0, [self.target.get_pos()], []))
			elif self.route == None or self.route == []:
				self.route = self.search.route(self.get_pos(), self.graph.get_graph(), self.furthest(self.get_pos()))[1:]
		


		if self.route == []:
			return False
		next_step = self.route[0]
		self.visited.append(next_step)
		self.route.remove(next_step)
		self.rect.x = next_step[1] * 30
		self.rect.y = next_step[0] * 30
		if next_step == self.target.get_pos():
			return False

		return next_step

	def furthest(self, pos):
		''' Return furthest state from current position '''
		furthest = None
		dist = 0
		for i in range(0, len(self.cells)):
			new_dist = len(self.search.route(pos, self.graph.get_graph(), self.cells[i]))
			if new_dist > dist:
				furthest = self.cells[i]
				dist = new_dist
		return furthest

	def check_deadlock(self):
			self.check =all(item in self.visited[-8:] for item in self.visited[-16:][:8])


	def max_p(self, pos, depth, target_actions, past):
		depth+=1
		actions = get_children(self.mazeObject.get_maze(), pos)
		max_option = -math.inf
		choice = None


		for action in actions:
			score = self.min_e(action, depth, target_actions, past, max_option)
			if score > max_option or choice == None:
				max_option = score
				choice = action

		if depth == 1:
			return choice
		else:
			return max_option
	
	def min_e(self, enemy_action, depth, target_actions, past, cur_max):
		for move in target_actions:
			actions = get_children(self.mazeObject.get_maze(), move)
			min = math.inf
			for action in actions:
				score = self.evaluationFunction(enemy_action, action, past)
				if depth < self.depth:
					score = score +self.max_p(enemy_action, depth, actions, copy(past))
				if score < min:
					min = score
				if depth == self.depth and score < cur_max: # Pruning 
					return score
		return min

	def evaluationFunction(self, state, target, past):
		''' Return score of state '''
		friends = []
		for enemy in self.enemies:
			friends.append(enemy.get_pos())
		score = 0
		if state == target:
			score += math.inf
		if state in friends or (state[0]+1, state[1]) in friends or (state[0]-1, state[1]) in friends or (state[0], state[1]+1) in friends or (state[0], state[1]-1) in friends:
			score -=math.inf
		else:
			dist = (abs(target[0] - state[0]) + abs(target[1] - state[1]))
			if dist == 0:
				dist = 1
			score += 1000/dist

		if state in past[-2:]:
			score -=100
		return score
	
	def add_enemy(self, enemy):
		self.enemies.append(enemy)