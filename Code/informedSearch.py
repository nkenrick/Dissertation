import math

from heuristic import *

'''
	Class for Greedy and A* search. Takes requested heuristic, method (display the search or the path) and search. 
'''
class Informed:
	def __init__ (self, heuristic, method, search):
		self.distance = None
		self.heuristic = heuristic
		self.method = method
		self.search = search 

	def route(self, start_node, graph, goal):
		h = Heuristic(goal, self.heuristic)

		explore = [(start_node, 0, [])] # Node, distance to node, children
		visited = []
		parents = {}
		parents[start_node] = None

		while  explore != []: # While there are still nodes to explore 

			cur_node = self.lowest(explore, h)
			if len(cur_node) == 3: # Adds nodes that lead to child node 
				visited = visited + cur_node[2]
 
			visited.append(cur_node[0])
			explore.remove(cur_node)

			if cur_node[0] == goal or goal in visited:
				self.distance = cur_node[1] # Distance taken to goal node

			
				if self.method == 'path':
					path = []
					current = (cur_node[0], [])                        
					while current is not None: # return path 
						path = path + current[1][::-1] # path to next node
						path.append(current[0])
						current = parents[current[0]]
						if current is not None and current[0] in path:
							current = None
					return path[::-1]
				else:
					return visited

			children = graph[cur_node[0]] # key = current node, value = list of children

			for child in children:
				if not self.in_explore(child, explore) and child[0] not in visited:
					explore.append((child[0], cur_node[1] + child[1], child[2])) # node, dist to node , children 
					if child[0] not in parents:
						parents[child[0]] = [cur_node[0], child[2]] # save parent node to work way backwards
				elif self.in_explore(child, explore):
					index = self.in_explore(child, explore)
					current = explore[index]
					if current[1] > cur_node[1] + child[1]:
						explore[index] = (child[0], child[1] + cur_node[1], child[2])
						if parents[cur_node[0]][0] != current[0]:
							parents[child[0]] = [cur_node[0], child[2]] # save parent node to work way backwards
		return []
	
	def lowest(self, explore, h):
		''' 
		Returns node with lowest path cost based on heuristic
		'''
		lowest = (None, math.inf)
		for i in range(len(explore)):
			new = explore[i]
			if lowest[0] == None:
				lowest = new
			elif self.search == 'A*' and (new[1] + h.value(new[0]) < lowest[1] + h.value(lowest[0])):
				lowest = new
			elif self.search == 'greedy' and(h.value(new[0]) < h.value(lowest[0])):
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
