import sys
import pygame
from GUI import GUI
from LearningUI import QGame
from button import Button
    

''' Main menu Gui, allows user to select search type'''
class Main_Menu(GUI):
    def __init__(self, visualise,  size, screen):
        super().__init__(visualise,  size, screen)
        self.informed_search_button = Button(pos=(40, 60), text="Informed Search", menu=self)
        in_w, in_h = self.informed_search_button.get_button_size()
        self.informed_search_button.update_pos(self.size - self.rect.w/2 - in_w/2, self.rect.h/2 + 50)

        self.uninformed_search_button = Button(pos=(40, 40), text="Uninformed Search", menu=self)
        un_w, un_h = self.uninformed_search_button.get_button_size()
        self.uninformed_search_button.update_pos(self.size - self.rect.w/2 - un_w/2, self.rect.h/2-50)

        self.q_learning_button = Button(pos=(40, 40), text="Q-Learning", menu=self)
        q_w, q_h = self.q_learning_button.get_button_size()
        self.q_learning_button.update_pos(self.size - self.rect.w/2 - q_w/2, self.rect.h/2+150)
    
    def draw(self):
        gui = pygame.sprite.Group()
        quit_button = Button(pos=(100, 20), text="QUIT", menu=self)
        quit_w, quit_h = quit_button.get_button_size()
        quit_button.update_pos(self.size - 20- quit_w, 20)

        if self.drawn == False:
            text = self.font.render("Hello, What would you like to visualise?", True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.rect.w/2, 150))
            self.screen.blit(text, text_rect)
            self.drawn = True



        gui.add(quit_button, self.uninformed_search_button, self.informed_search_button, self.q_learning_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if quit_button.rect.collidepoint(event.pos):
                    self.exit()
                elif self.informed_search_button.rect.collidepoint(event.pos):           
                    self.visualise.set_search_type('informed') #set search to informed
                
                elif self.uninformed_search_button.rect.collidepoint(event.pos):
                    self.visualise.set_search_type('uninformed')
                elif self.q_learning_button.rect.collidepoint(event.pos):
                    game = QGame(self.visualise)
                    game.draw()
                    

                gui.empty()

        return gui