import math
from copy import copy 
from graphRep import *
''' 
	Function used to find shortest route that traverses every cell in maze.

	This only returns a route of length 15 as it is being used by reflex agents so computing 
	the whole route takes too long, epecially since they most likely will have to change route at some point.
	If not, they simply compute the next 15 steps, this creates smoother visualisation.
'''

def traverseAll(start, mazeObject, search, goals):
	def nearest(pos, goal): #Find nearest goal to last node
		nearest = None
		dist = math.inf
		for i in range(0, len(goal)):
			if goal[i] in route:
				continue
			new_dist = len(search.route(pos, graph, goal[i]))
			if new_dist < dist:
				nearest = goal[i]
				dist = new_dist	
		return nearest

	def quick(pos, goal):  #Find nearest goal to last node, only check nodes that are directly ajacent 
		nearest = None
		dist = math.inf
		for i in range(0, len(goal)):
			if goal[i] in route:
				continue
			elif abs(goal[i][0] - pos[0]) > 1 or abs(goal[i][1] - pos[1]) > 1:
				continue
			new_dist = len(search.route(pos, graph, goal[i]))
			if new_dist < dist:
				nearest = goal[i]
				dist = new_dist	
		return nearest

	# Get all cells in maze 
	cells = mazeObject.get_cells()
	
	graph = Graph(mazeObject, (int(mazeObject.get_width()/2), int(mazeObject.get_height()/2)),cells).get_graph()

	route = [start]
	while goals != [] and len(route) <= 15: #Route shouldnt be longer then 15
		goal = None
		goal = quick(route[-1], goals)
		if goal is None:
			goal = nearest(route[-1], goals)
		if abs(goal[0] - route[-1][0]) > 1 or abs(goal[1] - route[-1][1]) > 1 or (abs(goal[0] - route[-1][0]) == 1 and abs(goal[1] - route[-1][1]) == 1): # Only need to get route if its not ajacent 
			route = route + search.route(route[-1], graph, goal)[1:]
		else:
			route.append(goal)

		goalscp = copy(goals)
		for i in range(0, len(goals)):
			x = goalscp[i]
			if x in route:
				goals.remove(x)
	return route[1:]