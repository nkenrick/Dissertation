from Agent import Agent
import numpy as np
from graphRep import *
from travereseAll import *

'''
Class for enemy reflex agent. Goal is agent if within 10 steps, otherwise searches for agent by going to its furthest point.
'''

class EnemyAgent(Agent):
	def __init__(self, x, y, search, mazeObject, target, colour):
		super().__init__(x, y, search, mazeObject, colour)
		self.target = target
		self.cells = mazeObject.get_cells()
		self.graph = Graph(mazeObject, (int(mazeObject.get_width()/2), int(mazeObject.get_height()/2)), 'ALL')

		self.chase = False
		self.visited = []
		self.RADIUS = 12
		self.check = False

	def move(self):

		# Check for deadlock
		if len(self.visited) >= 8:
			self.check_deadlock()

		if self.check:
			self.route = [self.get_pos()] # If in deadlock, stay still


		else:
			# Check if player in enemy sight radius
			if np.linalg.norm(np.asarray(self.get_pos())-np.asarray(self.target.get_pos())) > self.RADIUS:
				self.chase = False 
			else:
				self.chase = True	
			
			if self.chase:
				# Only invoke game theory algorithm if enemy is aware of the other player 
				route = self.search.route(self.get_pos(), self.graph.get_graph(), self.target.get_pos())[1:]
				if route[0] != self.visited[-1:]:
					self.route = route

			elif self.route == None or self.route == []:
				#If not chasing, go to furthest point
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
		''' Return furthest point in maze '''
		furthest = None
		dist = 0
		for i in range(0, len(self.cells)):
			new_dist = len(self.search.route(pos, self.graph.get_graph(), self.cells[i]))
			if new_dist > dist:
				furthest = self.cells[i]
				dist = new_dist
		return furthest

	def check_deadlock(self):
		self.check = all(item in self.visited[-4:] for item in self.visited[-8:][:4])
