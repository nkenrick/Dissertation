import numpy as np

'''Returns heuristic value of goal based on choice of heuristic'''

class Heuristic:
    def __init__(self, goal, type):
        self.goal = goal
        self.type = type 

    def value(self, node):
        if self.type == 'eclidean' or self.type == 'e':
            return np.linalg.norm(np.asarray(self.goal)-np.asarray(node))
        if self.type == 'manhattan' or self.type == 'm':
            return(abs(self.goal[0] - node[0]) + abs(self.goal[1] - node[1]))
        