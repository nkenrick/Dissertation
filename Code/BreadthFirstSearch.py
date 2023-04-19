from makeGraph import GraphVisualization
from getChildren import get_children

'''
Method performs a BFS on the graph(maze) and returns an action /search
sequence for our agent to use (order of states to visit).

Also creates a graph object for visualisation - not used for testing so not returned.
'''
class BFS:
	def route(self, initial_state, mazeObject, goal):
		''' Returns when goal found, or if there is not goal once it has traversed entire maze'''
		maze = mazeObject.get_maze()
		explore = [initial_state]
		visited = []
		G = GraphVisualization()
		cont = True
		while explore != [] and cont:
			state = explore[0]
			explore.remove(state)
			visited.append(state)
			if goal != None and goal == state:
				cont = False
			else:
				children = get_children(maze, state)
				if children != []:
					for child in children:
						G.add_edge(state, child)
						if child not in explore and child not in visited:
							explore.append(child)
		return visited 
		


	
