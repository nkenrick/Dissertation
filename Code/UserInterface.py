from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sys
import pygame
from MainMenu import Main_Menu
from SearchSelect import  UninformedSelect, InformedSelect
from UninformedGameGui import *
from EndgameUI import EndgameUI
pygame.init()

'''Main class for the Uuser interface'''

class Visulaise():
    def __init__(self):
        self.game_state = 'menu'
        self.search_type = None
        self.select = None
        self.size = 600
        self.maze_size = 'medium'
        self.screen = pygame.display.set_mode((self.size, self.size))
        self.menu = Main_Menu(self, self.size,self.screen)
        self.search = None
        self.end = None
        self.maze = None

    def update_game_state(self, new_game_state):
        self.game_state = new_game_state

    def set_search_type(self, type):
        self.search_type = type
        self.game_state = 'algorithm_select'
        if self.search_type == 'informed':
            self.search = InformedSelect(self, self.size, self.screen)
        else:
            self.search = UninformedSelect(self, self.size, self.screen)

    def end_game(self, state, time_taken, steps, maze, learning=False):
        self.end = EndgameUI(self, self.size, self.screen, state, time_taken, steps, maze, learning)
        self.update_game_state('end_game')
    
    def save_maze(self, maze):
        self.maze = maze
    
    def get_maze(self):
        return self.maze

    def main(self):
        running = True 

        gui = pygame.sprite.Group()

        while running:
            if self.game_state == 'menu':
                self.menu.setup('Menu')
                gui = self.menu.draw()

            elif self.game_state == 'maze_select':
                gui = self.select.draw()


            elif self.game_state == 'algorithm_select':
                if self.search_type== 'uninformed':
                    self.search.setup('Uninformed Algorithms')

                else:
                    self.search.setup('Informed Algorithms')
                gui = self.search.draw()
            
            elif self.game_state == 'end_game':
                self.end.setup('Game End')
                gui = self.end.draw()


            gui.update() 
            gui.draw(self.screen)
            pygame.display.flip()

if __name__ == "__main__":
    start = Visulaise()
    start.main()