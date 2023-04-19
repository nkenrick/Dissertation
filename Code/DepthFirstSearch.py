from getChildren import get_children

'''
Method performs a DFS on the graph (maze) and returns an action 
sequence for our agent to use (order of states to visit)
'''

class DFS:
	def route(self, state, mazeObject, goal):
		maze = mazeObject.get_maze()
		explore = [state]
		visited = []
		cont = True
		init_state = state
		while cont and explore != []:
			state = explore.pop()
			visited.append(state)
			if goal != None and state == goal:
				cont = False
			else:
				children = get_children(maze, state)
				for child in children:
					if child not in explore and child not in visited:
						explore.append(child)
		return visited
