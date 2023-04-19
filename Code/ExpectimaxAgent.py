from MinMaxAgent import MinMaxAgent
import math
import numpy as np
from graphRep import *
from travereseAll import *

'''
	Class for player agent that uses Expectimax algorithm. Inherits from MinMaxAgent.
'''
class ExpectimaxAgent(MinMaxAgent):
	def __init__(self, x, y, search, mazeObject, goal, colour, game):
		super().__init__(x, y, search, mazeObject, goal, colour, game)

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
		if len(self.visited) >= 8:
			self.check_deadlock()

		past.append(pos)


		if self.check:
			return self.run(pos, self.closest(pos))

		for action in actions:
			score = self.chance(action, depth, enemy_actions, past, max_option)
			if score > max_option or choice == None:
				max_option = score
				choice = action

		if depth == 1:
			return choice
		else:
			return max_option
	
	def chance(self, player_action, depth, enemy_actions,past, cur_max):
		for enemy_move in enemy_actions:
			actions = get_children(self.mazeObject.get_maze(), enemy_move)
			actions.append(enemy_move)
			
			score = 0
			for action in enemy_actions:
				score = score + self.evaluationFunction(player_action, action,past)
				if depth < self.depth:
					score = score +self.max_p(player_action, depth, actions,copy(past))
		score = score /len(enemy_actions)
		return score