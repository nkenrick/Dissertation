import unittest
from DepthFirstSearch import DFS
from mazeGenerator import *

'''
Uses TDD to make sure that our DFS behaves correctly
'''

class MyTests(unittest.TestCase):

	def setUp(self):
		mazeRead = open("testMaze.txt", "r") # Have a specific testmaze so can set goals and test accuratly
		self.mazeObject = Maze(12, 12, mazeRead.read())
		mazeRead.close()
		self.dfs = DFS()

	def test_returns(self):
		self.assertIsNotNone(self.dfs.route((6,6), self.mazeObject.get_maze(), None))
	
	def test_visits_every_node(self):
		result = self.dfs.route((6, 6), self.mazeObject.get_maze(), None)
		self.assertTrue(len(result), 70)

	def test_goal(self):
		result = self.dfs.route((6, 6), self.mazeObject.get_maze(), (10, 6))
		self.assertTrue(result[-1] == (10, 6), True)
