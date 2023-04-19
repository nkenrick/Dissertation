import unittest
from BreadthFirstSearch import BFS
from mazeGenerator import *

'''
Uses TDD to make sure that our BFS behaves correctly
'''

class MyTests(unittest.TestCase):
	
	def setUp(self):
		mazeRead = open("testMaze.txt", "r") # Have a specific testmaze so can set goals and test accuratly
		self.mazeObject = Maze(12, 12, mazeRead.read())
		mazeRead.close()
		self.bfs = BFS()

	def test_returns(self):
		self.assertIsNotNone(self.bfs.route((6,6), self.mazeObject.get_maze(), None))

	def test_visits_every_node(self):
		self.assertEqual(len(self.bfs.route((6, 6), self.mazeObject.get_maze(), None)), 70) # TestMaze has 70 nodes	

	def test_turn_left_first(self):
		returned = (self.bfs.route((6, 6), self.mazeObject.get_maze(),None))
		self.assertEqual(returned[1], (5,6))

	def test_end_node(self):
		returned = (self.bfs.route((6, 6), self.mazeObject.get_maze(), None))
		self.assertEqual(returned[len(returned)-1], (1, 5))

	def test_end_goal(self):
		returned = (self.bfs.route((6, 6), self.mazeObject.get_maze(), (4, 6)))
		self.assertEqual(returned[-1] == (4, 6), True)
