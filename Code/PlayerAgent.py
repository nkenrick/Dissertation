from Agent import Agent
import math
import numpy as np
from graphRep import *
from travereseAll import *
'''
Class for player reflex agent. find route to traverse and collect every goal, runs if too close to enemy agent.
'''
class PlayerAgent(Agent):
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
		self.reaval = []
		self.visited = [(x, y)]
		self.check = False


	def move(self):
		if self.goal == []:
			return True
		run_from = None
		
		self.reaval = []
		for enemy in self.villans:
			if self.get_pos() == enemy.get_pos():
				self.game.finished()
			if (abs(self.get_pos()[0] - enemy.get_pos()[0]) + abs(self.get_pos()[1] - enemy.get_pos()[1])) <=3:
				self.reaval.append(True)
				run_from = enemy.get_pos()
			else:
				self.reaval.append(False)

		if len(self.visited) >= 16:
			self.check_deadlock()
			
		if self.check:
			self.route = self.run(self.get_pos(), self.get_pos())
		else:
			if True in self.reaval:
				self.route= self.furthest(self.get_pos(), run_from, copy(self.goal))
			elif self.route == None or self.route ==[]:		
				self.route=traverseAll(self.get_pos(), self.mazeObject, self.search, copy(self.goal))
		


		if self.route != []:
			next_step = self.route[0]
			self.route.remove(next_step)
			if next_step in self.goal:
				self.goal.remove(next_step)
			self.rect.x = next_step[1] * 30
			self.rect.y = next_step[0] * 30
			self.visited.append(next_step)
			return next_step

	def check_deadlock(self):	
		self.check =  all(item in self.visited[-8:] for item in self.visited[-16:][:8])

	def nearest(self, pos):
		''' Return nearest state with item to collect '''
		nearest = None
		dist = math.inf 
		for i in range(0, len(self.goal)):
			new_dist = len(self.search.route(pos, self.graph.get_graph(), self.goal[i]))
			if new_dist < dist:
				nearest = self.goal[i]
				dist = new_dist
			if new_dist == dist and np.linalg.norm(np.asarray(pos)-np.asarray(nearest)) > np.linalg.norm(np.asarray(pos)-np.asarray(self.goal[i])):
				nearest = self.goal[i]
				dist = new_dist
		return nearest

	def furthest(self, pos, enemy_pos, goals):
		''' Return furthest state from player '''
		cont = True
		while cont and goals != []:
			furthest = None
			dist = 0
			for i in range(0, len(goals)):
				new_dist = len(self.search.route(enemy_pos, self.graph.get_graph(), goals[i]))
				if new_dist > dist:
					furthest = goals[i]
					dist = new_dist
			if furthest != None:
				''' Make sure route doesnt pass through enemy'''
				route = self.search.route(self.get_pos(), self.graph.get_graph(), furthest)[1:]
				if enemy_pos not in route and (route[0] not in get_children(self.mazeObject.get_maze(), enemy_pos)):
					return route
				else:
					goals.remove(furthest)
			else:
				cont = False
		return self.run(pos, enemy_pos)
		
	def run(self, pos, enemy_pos):
		''' Return furthest state from enemy '''
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
		return [choice]

	def add_villan(self, villan):
		self.villans.append(villan)