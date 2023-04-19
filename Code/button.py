import pygame

''' Class for all buttons used in user interface'''

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, text, menu):
        super().__init__()
        self.text = text
        self.text_surf = menu.font.render(text, True, (0, 0, 0))
        self.image = pygame.Surface((self.text_surf.get_width()+40, self.text_surf.get_height()+20))
        self.colour = (255, 255, 255)
        self.image.fill(self.colour)
        self.image.blit(self.text_surf, (20, 10))
        self.pos = pos
        self.rect = self.image.get_rect(topleft=self.pos)
        self.clicked = False

    def get_text(self): # Return text of button
        return self.text
    
    def update_pos(self, x, y): 
        self.pos = (x, y)
        self.rect = self.image.get_rect(topleft=self.pos)
    
    def get_button_size(self):
        return self.image.get_width(), self.image.get_height()
    
    def change_colour(self):
        if self.colour == (0, 115, 141):
            self.colour = (255, 255, 255)
        else:
            self.colour = (0, 115, 141)
        self.image.fill(self.colour)
        self.image.blit(self.text_surf, (20, 10))

    def unavailable(self): # Set button to unavailable 
        self.colour = (168, 168, 168)
        self.image.fill(self.colour)
        self.image.blit(self.text_surf, (20, 10))

    def available(self): # Set button to available 
        self.colour = (255, 255, 255)
        self.image.fill(self.colour)
        self.image.blit(self.text_surf, (20, 10))