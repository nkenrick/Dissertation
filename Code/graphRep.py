from getChildren import get_children
'''
Given a maze and a start node, constructs a graph represented as a dictionary.

The key is a node, the value is a list of child nodes. Each child node is a list
with the nodes it must travel to get there, along with path cost.
'''
class Graph:
	def __init__(self, maze, node, goal):
		self.node = node
		self.maze = maze.get_maze()
		if goal == 'ALL': 
			self.goal = maze.get_cells()
		else:
			self.goal = goal
		self.graph = self.make_graph()

	def get_graph(self):
		return self.graph

	def make_graph(self):
		graph = {}
		nodes = {self.node}
		visited = []
		while len(nodes) != 0:
			cur_node = nodes.pop()
			graph[cur_node] = []
			children = get_children(self.maze, cur_node)
			for child in children:
				if len(get_children(self.maze, child)) == 1: # One child means it is a 'leaf' node
					graph[cur_node].append([child, 1, []])
					graph[child] = [[cur_node, 1, []]]
				elif len(get_children(self.maze, child)) >=3: # 3 or more children means its not just a path
					graph[cur_node].append([child, 1, []])
					if child not in nodes and child not in visited:
						nodes.add(child)
				else:
					dist, new_node, path= self.find_next_node(0, child, cur_node, []) 

					graph[cur_node].append([new_node, dist, path])
					if new_node not in nodes and new_node not in visited:
						nodes.add(new_node)
			visited.append(cur_node)
		return graph

	def find_next_node(self, count, cur_node, prev_node, path):
		children = get_children(self.maze, cur_node)
		count += 1
		
		if len(children) == 1 or len(children) >=3 or cur_node in self.goal: # Goal can be anywhere, need to identify it as a node 
			return count, cur_node, path

		else:
			if children[0] == prev_node:
				path.append(cur_node)
				return self.find_next_node(count, children[1], cur_node, path)
			else:
				path.append(cur_node)
				return self.find_next_node(count, children[0], cur_node, path)
