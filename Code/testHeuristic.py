import unittest
import numpy as np
from heuristic import *

'''
Uses TDD to make sure that our heuristics return the correct value 
'''

class MyTests(unittest.TestCase):
	
    def setUp(self) -> None:
        self.goal = (3, 3)
        self.start = (0, 0)  

    def test_returns_eclidean(self):
        h = Heuristic(self.goal, 'eclidean')
        self.assertEqual(h.value(self.start), 4.242640687119285)

    def test_returns_eclidean(self):
        h = Heuristic(self.goal, 'manhattan')
        self.assertEqual(h.value(self.start), 6)

    def test_multiple_eclidean(self):
        h = Heuristic(self.start, 'eclidean')
        self.assertEqual(h.value( (3, 4)), 5)
        self.assertEqual(h.value((2, 3)), 3.605551275463989)
        self.assertEqual(h.value((2, 2)), 2.8284271247461903)
    
    def test_mutiple_manhattan(self):
        h = Heuristic(self.start, 'manhattan')
        self.assertEqual(h.value( (3, 4)), 7)
        self.assertEqual(h.value((2, 3)), 5)
        self.assertEqual(h.value((2, 2)), 4)