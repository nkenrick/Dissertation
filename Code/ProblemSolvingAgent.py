from Agent import Agent
'''
Class for problem solving agent. Recieves an action sequence given 
to it by an uninfomed search
'''
class ProblemSolvingAgent(Agent):
	def __init__(self, x, y, search, mazeObject, goal, colour):
		super().__init__(x, y, search, mazeObject, colour)
		#For search
		self.start_coord= (x, y)
		self.goal = goal

	def move(self):
		if self.route == None:
			self.route= self.search.route(self.start_coord, self.mazeObject, self.goal)
		
		if self.route != []:
			next_step = self.route[0]
			self.route.remove(next_step)
			self.rect.x = next_step[1] * 30
			self.rect.y = next_step[0] * 30
			if next_step == self.goal:
				self.route = []
			return next_step
		return True

