from MinMaxEnemyAgent import MinMaxEnemyAgent
import numpy as np
from graphRep import *
from travereseAll import *
'''
Class for Expectimax Enemy agent. Goal is agent if within given radius, otherwise searches for agent by going to the furthest point from it on the maze.
'''
class ExpectimaxEnemy(MinMaxEnemyAgent):
	def __init__(self, x, y, search, mazeObject, target, colour, game, radius):
		super().__init__(x, y, search, mazeObject, target, colour, game, radius)

	def move(self):

		if self.get_pos() == self.target.get_pos():
			self.game.finished() # Game Over

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
				if len(self.visited) <= 2:
					self.route.append(self.max_p(self.get_pos(), 0, [self.target.get_pos()], []))
				else:
					self.route.append(self.max_p(self.get_pos(), 0, [self.target.get_pos()], [self.visited[-2]]))

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


	def max_p(self, pos, depth, target_actions, past):
		depth+=1
		actions = get_children(self.mazeObject.get_maze(), pos)
		max_option = -math.inf
		choice = None

		for action in actions:
			score = self.chance(action, depth, target_actions, past, max_option)
			if score > max_option or choice == None:
				max_option = score
				choice = action
		if depth == 1:
			return choice
		else:
			return max_option
	
	def chance(self, enemy_action, depth, target_actions,past, cur_max):
		for enemy_move in target_actions:
			actions = get_children(self.mazeObject.get_maze(), enemy_move)
			actions.append(enemy_move)
			
			score = 0
			for action in target_actions:
				score = score + self.evaluationFunction(enemy_action, action,past)
				if depth < self.depth:
					score = score +self.max_p(enemy_action, depth, actions,copy(past))
		score = score /len(target_actions)
		return score
