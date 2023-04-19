import sys
import pygame

''' Standard setup for most interfaces implemented '''

class GUI():
    def __init__(self, visualise, size, screen):
        self.screen = screen
        self.size = size
        self.rect = self.screen.get_rect()
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25)
        self.menu_open = True
        self.drawn = False
        self.visualise = visualise

    def setup(self, title):
        self.size = self.visualise.size
        self.rect = self.screen.get_rect()
        self.screen.fill((0, 141, 97))
        pygame.display.set_caption(title)
        self.drawn = False

    def exit(self):
        self.screen.fill((0, 141, 97))
        text = self.font.render("Goodbye!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.rect.w/2, self.rect.h/2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.quit()
        sys.exit()