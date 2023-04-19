from Agent import Agent
import math
import numpy as np
from graphRep import *
from travereseAll import *
'''
Class for informed search problem solving agent. Recieves an action sequence given 
to it by an infomed search
'''
class InformedAgent(Agent):
	def __init__(self, x, y, search, mazeObject, goal, colour):
		super().__init__(x, y, search, mazeObject, colour)
		self.goal = []
		if goal == 'all': ## Get route to traverse entire maze 
			self.route = traverseAll(self.get_pos(), mazeObject, search)
		elif not isinstance(goal, list): # Allows for multiple goals
			self.goal = [goal] 
		else:
			self.goal = goal
		self.graph = Graph(mazeObject.get_maze(), (int(mazeObject.get_width()/2), int(mazeObject.get_height()/2)), self.goal)

	def move(self):
		if self.route == None:
			self.route=[self.get_pos()]
			while self.goal != []:
				goal = self.nearest(self.route[-1])
				self.goal.remove(goal)
				self.route = self.route + self.search.route(self.route[-1], self.graph.get_graph(), goal)
	

		if self.route != []:
			next_step = self.route[0]
			self.route.remove(next_step)
			self.rect.x = next_step[1] * 30
			self.rect.y = next_step[0] * 30
			if next_step == self.goal:
				self.route = []
			return next_step
		return True

	def nearest(self, pos):
		nearest = None
		dist = math.inf 
		for i in range(0, len(self.goal)):
			new_dist = len(self.search.route(self.route[-1], self.graph.get_graph(), self.goal[i]))
			if new_dist < dist:
				nearest = self.goal[i]
				dist = new_dist
			if new_dist == dist and np.linalg.norm(np.asarray(self.route[-1])-np.asarray(nearest)) > np.linalg.norm(np.asarray(self.route[-1])-np.asarray(self.goal[i])):
				nearest = self.goal[i]
				dist = new_dist
		return nearest

