import math
from graphRep import *
'''
Method performs a UCS on the graph and returns an action 
sequence for our agent to use (order of states to visit) 
as well as distance to get there (for testing perposes)
'''
class UCS:
	def __init__ (self):
		self.distance = None

	def route(self, start_node, mazeObject, goal):
		graphObject = Graph(mazeObject, (int(mazeObject.get_width()/2), int(mazeObject.get_height()/2)), [goal, start_node])
		graph = graphObject.get_graph()
		explore = [(start_node, 0, [])]
		visited = []
		while  explore != []:
			cur_node = self.lowest(explore)
			if len(cur_node) == 3:
				visited = visited + cur_node[2]
			visited.append(cur_node[0])
			explore.remove(cur_node)
			if cur_node[0] == goal or goal in visited:
				self.distance = cur_node[1]
				return visited
			children = graph[cur_node[0]]
			for child in children:
				if not self.in_explore(child, explore) and child[0] not in visited:
					explore.append((child[0], cur_node[1] + child[1], child[2]))
				elif self.in_explore(child, explore):
					index = self.in_explore(child, explore)
					current = explore[index]
					if current[1] > cur_node[1] + child[1]:
						explore[index] = (child[0], child[1] + cur_node[1], child[2])
		return visited
	
	def lowest(self, explore):
		''' 
		Returns node with lowest path cost
		'''
		lowest = (None, math.inf)
		for i in range(len(explore)):
			new = explore[i]
			if new[1] < lowest[1]:
				lowest = new
		return lowest

	def in_explore(self, child, explore):
		'''
		Check if we have already visited a node
		'''
		for i in range(0, len(explore)):
			if child[0] == explore[i][0]:
				return i
		return False

	def get_distance(self):
		return self.distance
