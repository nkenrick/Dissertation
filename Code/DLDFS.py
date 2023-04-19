from getChildren import get_children
import math

'''
Method performs a Depth Limited search on the graph (maze) and returns an action 
sequence for our agent to use (order of states to visit)
'''

class DLDFS:
	def route(self, init_state, mazeObject, goal):
		maze = mazeObject.get_maze()
		explore = [init_state]
		visited = []
		cont = True
		limit = math.inf
		if goal != None:
			limit = max(abs(init_state[0] - goal[0]), abs(init_state[1] - goal[1]))
		while cont and explore != []:
			state = explore.pop()
			visited.append(state)
			if goal != None and state == goal:
				cont = False
			else:
				children = get_children(maze, state)
				for child in children:
					if abs(child[0]-init_state[0]) > limit or abs(child[1]-init_state[1])>limit:
						continue
					elif child not in explore and child not in visited:
						explore.append(child)
		return visited
