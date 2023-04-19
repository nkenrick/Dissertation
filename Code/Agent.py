import pygame
'''
Super class for agents. 
'''
class Agent(pygame.sprite.Sprite):
	def __init__(self, x, y, search, mazeObject, colour):
		# Create sprite for visulaisation 
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([24,24])
		self.image.fill(colour)
		self.colour = colour
		self.rect = self.image.get_rect()
		self.rect.x = x*30 +3
		self.rect.y = y*30 +3

		# For search
		self.mazeObject = mazeObject
		self.route = None
		self.search = search

	def get_pos(self):
		# Return current position
		return (int(self.rect.y / 30), int(self.rect.x/30))

	def draw(self, surface):
		# Draw to screen
		if self.rect.x % 2 == 0:
			self.rect.x = self.rect.x +3
			self.rect.y = self.rect.y +3
		pygame.draw.rect(surface, self.colour, self.rect)