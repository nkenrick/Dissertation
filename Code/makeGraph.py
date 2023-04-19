import networkx as nx
import matplotlib.pyplot as plt

'''
Constructs a visullisation of the maze as a graph using the libraries
networkx and matplotlib
'''

class GraphVisualization:

	def __init__(self):
		self.visual = []

	def visualize(self):
		G = nx.Graph()
		G.add_edges_from(self.visual)
		pos = nx.spring_layout(G)
		nx.draw_networkx(G,pos,  node_size=50, font_size=10, width=2)
		plt.show()

	def add_edge(self, node1, node2):
		edge = [node1, node2]
		self.visual.append(edge)

