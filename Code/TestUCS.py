import unittest
from UniformCostSearch import UCS
from mazeGenerator import *
from graphRep import *

'''
Uses TDD to make sure that our UCS behaves correctly
'''

class MyTests(unittest.TestCase):
	
	def setUp(self):
		mazeRead = open("testMaze.txt", "r") # Have a specific testmaze so can set goals and test accuratly
		self.mazeObject = Maze(12, 12, mazeRead.read())
		mazeRead.close()
		self.ucs = UCS()

	def test_returns(self):
		self.assertIsNotNone(self.ucs.route((6, 6), self.mazeObject, (6, 6)))

	def test_returns_fake(self):
		result = self.ucs.route((6, 6), self.mazeObject, (6, 8))
		self.assertEqual(self.ucs.get_distance(), 2) 

	def test_returns_actual(self):
		result = self.ucs.route((6, 6), self.mazeObject, (8, 8))
		self.assertEqual(self.ucs.get_distance(), 4) 
	
