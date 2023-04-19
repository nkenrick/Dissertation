import pygame
from button import Button
from GUI import GUI
from UninformedGameGui import Game
from InformedGameGui import IGame
from BreadthFirstSearch import BFS
from UniformCostSearch import UCS
from DepthFirstSearch import DFS

class UninformedSelect(GUI):
    def __init__(self, visualise, size, screen):
            super().__init__(visualise,  size, screen)

            self.maze = visualise.get_maze()

            # Select maze size options
            self.large_maze_btn = Button(pos=(40, 40), text="Large", menu=self)
            l_w, l_h = self.large_maze_btn.get_button_size()
            self.large_maze_btn.update_pos(20, 80)

            self.medium_maze_btn = Button(pos=(40, 60), text="Medium (recommended)", menu=self)
            m_w, m_h = self.medium_maze_btn.get_button_size()
            self.medium_maze_btn.update_pos(self.size - self.rect.w/2 - m_w/2, 80)

            self.small_maze_btn = Button(pos=(40, 80), text="Small", menu=self)
            s_w, s_h = self.small_maze_btn.get_button_size()
            self.small_maze_btn.update_pos(self.size - s_w - 20, 80)

            #Select Algorithm
            self.algo1 = Button(pos=(40, 40), text="Breadth First Search", menu=self)
            w1, h1 = self.algo1.get_button_size()
            self.algo1.update_pos(self.size - self.rect.w/2 - w1/2, 190)

            self.algo2 = Button(pos=(40, 60), text="Depth First Search", menu=self)
            w2, h2 = self.algo2.get_button_size()
            self.algo2.update_pos(self.size - self.rect.w/2 - w2/2, 250)

            self.algo3 = Button(pos=(40, 80), text="Uniform Cost Search", menu=self)
            w3, h3 = self.algo3.get_button_size()
            self.algo3.update_pos(self.size - self.rect.w/2 - w3/2, 310)
        
            # Select goal position options
            self.corner_btn = Button(pos=(40, 40), text="Corner", menu=self)
            c_w, c_h = self.corner_btn.get_button_size()
            self.corner_btn.update_pos(self.size - self.rect.w/4 - c_w/2, 420)

            self.random_btn  = Button(pos=(40, 60), text="Random", menu=self)
            r_w, r_h = self.random_btn .get_button_size()
            self.random_btn .update_pos(self.size - self.rect.w/4 - r_w/2, 480)

            self.centre_btn = Button(pos=(40, 80), text="Centre", menu=self)
            co_w, co_h = self.centre_btn.get_button_size()
            self.centre_btn.update_pos(self.size - self.rect.w/4- co_w /2, 540)

            # Select start position option 
            self.corner_btn_2 = Button(pos=(40, 40), text="Corner", menu=self)
            c2_w, c2_h = self.corner_btn_2.get_button_size()
            self.corner_btn_2.update_pos(self.rect.w/4 - c2_w/2, 420)

            self.random_btn_2 = Button(pos=(40, 60), text="Random", menu=self)
            r2_w, r2_h = self.random_btn_2.get_button_size()
            self.random_btn_2.update_pos(self.rect.w/4 - r2_w/2, 480)

            self.centre_btn_2 = Button(pos=(40, 80), text="Centre", menu=self)
            co2_w, co2_h = self.centre_btn_2.get_button_size()
            self.centre_btn_2.update_pos(self.rect.w/4 - co2_w /2, 540)

            self.algo_choice = None
            self.maze_choice = self.medium_maze_btn
            self.medium_maze_btn.change_colour()
            self.start_choice = self.random_btn_2
            self.random_btn_2.change_colour()
            self.goal_choice = self.random_btn
            self.random_btn.change_colour()

            self.goal_unavailable = None
            self.start_unavailable = None

    def draw(self):
        self.maze = self.visualise.get_maze()
        w, h = pygame.display.get_surface().get_size()
        if w != 600:
            self.screen = pygame.display.set_mode((600, 600))
        
        gui = pygame.sprite.Group()

        if self.drawn == False:
            quit_button = Button(pos=(100, 20), text="QUIT", menu=self)
            quit_w, quit_h = quit_button.get_button_size()
            quit_button.update_pos(self.size - 20- quit_w, 20)

            back_button = Button(pos=(20, 20), text="Back", menu=self)

            text = self.font.render("Select Maze Size", True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.rect.w/2, 50))
            self.screen.blit(text, text_rect)

            a_text = self.font.render("Select Algorithm", True, (0, 0, 0))
            a_text_rect = a_text.get_rect(center=(self.rect.w/2, 160))
            self.screen.blit(a_text, a_text_rect)

            start_text = self.font.render("Select Start Position", True, (0, 0, 0))
            start_text_rect = start_text.get_rect(center=(self.rect.w/4, 390))
            self.screen.blit(start_text, start_text_rect)

            goal_text = self.font.render("Select Goal Position", True, (0, 0, 0))
            goal_text_rect = goal_text.get_rect(center=(self.size - self.rect.w/4, 390))
            self.screen.blit(goal_text, goal_text_rect)
            self.drawn = True

            gui.add(quit_button, self.algo1, self.algo2, self.algo3, self.large_maze_btn, self.medium_maze_btn, self.small_maze_btn, self.corner_btn, self.centre_btn, self.random_btn , \
                self.corner_btn_2, self.centre_btn_2, self.random_btn_2, back_button)

        if self.algo_choice != None and self.maze_choice != None and self.start_choice != None and self.goal_choice != None:
            go_btn = Button(pos=(40, 80), text="Go!", menu=self)
            go_w, go_h = go_btn.get_button_size()
            go_btn.update_pos(self.size - self.rect.w/2 - go_w/2, 480)
            gui.add(go_btn)
        else:
            go_btn = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if quit_button.rect.collidepoint(event.pos):
                    self.exit()
                elif self.algo1.rect.collidepoint(event.pos):
                    self.algo_choice = self.button_select(self.algo_choice, self.algo1)

                elif self.algo2.rect.collidepoint(event.pos):
                    self.algo_choice = self.button_select(self.algo_choice, self.algo2)

                elif self.algo3.rect.collidepoint(event.pos):
                   self.algo_choice = self.button_select(self.algo_choice, self.algo3)

                elif self.large_maze_btn.rect.collidepoint(event.pos):
                    self.maze_choice = self.button_select(self.maze_choice, self.large_maze_btn)
                
                elif self.medium_maze_btn.rect.collidepoint(event.pos):
                    self.maze_choice = self.button_select(self.maze_choice, self.medium_maze_btn)

                elif self.small_maze_btn.rect.collidepoint(event.pos):
                    self.maze_choice = self.button_select(self.maze_choice, self.small_maze_btn)

                elif self.corner_btn_2.rect.collidepoint(event.pos):
                    self.start_choice = self.start_position(self.start_choice, self.corner_btn_2, self.corner_btn)

                elif self.random_btn_2.rect.collidepoint(event.pos):
                    self.start_choice = self.start_position(self.start_choice, self.random_btn_2, None)
                
                elif self.centre_btn_2.rect.collidepoint(event.pos):
                    self.start_choice = self.start_position(self.start_choice, self.centre_btn_2, self.centre_btn)

                elif self.corner_btn.rect.collidepoint(event.pos):
                    self.goal_choice = self.goal_position(self.goal_choice, self.corner_btn, self.corner_btn_2)

                elif self.random_btn.rect.collidepoint(event.pos):
                    self.goal_choice = self.goal_position(self.goal_choice, self.random_btn, None)
                
                elif self.centre_btn.rect.collidepoint(event.pos):
                    self.goal_choice = self.goal_position(self.goal_choice, self.centre_btn,self.centre_btn_2)
                
                elif back_button.rect.collidepoint(event.pos):
                    self.visualise.update_game_state('menu')
                if go_btn in gui:
                    if go_btn.rect.collidepoint(event.pos):
                        if self.algo_choice == self.algo1:
                            search = BFS()

                        elif self.algo_choice == self.algo2:
                            search = DFS()
                        
                        else:
                            search = UCS()
                        game = Game(self.visualise,  search, self.maze_choice.get_text(), self.start_choice.get_text(), self.goal_choice.get_text(), self.maze)
                        game.draw()


                gui.empty()
        
        return gui
    
    def button_select(self, choice, new): 
        if choice != None:
           choice.change_colour()
        choice = new
        new.change_colour()
        return new
    
    def start_position(self, choice, new, sibling): 
        if new != self.start_unavailable:
            if choice != None:
                choice.change_colour()
            choice = new
            new.change_colour()
            if self.goal_unavailable != None:
                self.goal_unavailable.available()

            self.goal_unavailable = sibling
            if sibling!= None:
                sibling.unavailable()
            return new
        return choice
    
    def goal_position(self, choice, new, sibling): 
        if new != self.goal_unavailable:
            if choice != None:
                choice.change_colour()
            choice = new
            new.change_colour()
            if self.start_unavailable != None:
                self.start_unavailable.available()

            self.start_unavailable = sibling
            if sibling != None:
                sibling.unavailable()
            return new
        return choice
    

class InformedSelect(UninformedSelect):
    def __init__(self, visualise, size, screen):
        super().__init__(visualise,  size, screen)
        #Select Algorithm
        self.algo1 = Button(pos=(40, 40), text="A* Search", menu=self)
        w1, h1 = self.algo1.get_button_size()
        self.algo1.update_pos(self.size - self.rect.w/2 - w1/2, 190)

        self.algo2 = Button(pos=(40, 60), text="MinMax with alpha-beta pruning", menu=self)
        w2, h2 = self.algo2.get_button_size()
        self.algo2.update_pos(self.size - self.rect.w/2 - w2/2, 250)

        self.algo3 = Button(pos=(40, 80), text="Expectimax", menu=self)
        w3, h3 = self.algo3.get_button_size()
        self.algo3.update_pos(self.size - self.rect.w/2 - w3/2, 310)

        self.one_enemy = Button(pos=(40, 40), text="One", menu=self)
        one_w, one_h = self.one_enemy.get_button_size()
        self.one_enemy.update_pos(self.rect.w/4 - one_w/2, 420)

        self.two_enemy  = Button(pos=(40, 60), text="Two", menu=self)
        two_w, two_h = self.two_enemy .get_button_size()
        self.two_enemy .update_pos(self.rect.w/4 - two_w/2, 480)

        self.three_enemy = Button(pos=(40, 80), text="Three", menu=self)
        three_w, three_h = self.three_enemy.get_button_size()
        self.three_enemy.update_pos(self.rect.w/4- three_w /2, 540)

        self.enemy_choice = self.two_enemy
        self.two_enemy.change_colour()
        self.num_enemys = 2
   
        
            
    def draw(self):
        self.maze = self.visualise.get_maze()
        w, h = pygame.display.get_surface().get_size()
        if w != 600:
            self.screen = pygame.display.set_mode((600, 600))
        
        gui = pygame.sprite.Group()

        if self.drawn == False:
            quit_button = Button(pos=(100, 20), text="QUIT", menu=self)
            quit_w, quit_h = quit_button.get_button_size()
            quit_button.update_pos(self.size - 20- quit_w, 20)

            back_button = Button(pos=(20, 20), text="Back", menu=self)
            
            text = self.font.render("Select Maze Size", True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.rect.w/2, 50))
            self.screen.blit(text, text_rect)

            a_text = self.font.render("Select Algorithm", True, (0, 0, 0))
            a_text_rect = a_text.get_rect(center=(self.rect.w/2, 160))
            self.screen.blit(a_text, a_text_rect)
            self.drawn = True

            start_text = self.font.render("Select number of enemies", True, (0, 0, 0))
            start_text_rect = start_text.get_rect(center=(self.rect.w/4, 390))
            self.screen.blit(start_text, start_text_rect)
            gui.add(quit_button, self.algo1, self.algo2, self.algo3, self.large_maze_btn, self.medium_maze_btn, self.small_maze_btn, back_button, self.one_enemy, self.one_enemy, self.two_enemy, self.three_enemy)


        if self.algo_choice != None and self.maze_choice != None:
            go_btn = Button(pos=(40, 80), text="Go!", menu=self)
            go_w, go_h = go_btn.get_button_size()
            go_btn.update_pos(self.size - self.rect.w/2 - go_w/2, 480)
            gui.add(go_btn)
        else:
            go_btn = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if quit_button.rect.collidepoint(event.pos):
                    self.exit()
                elif back_button.rect.collidepoint(event.pos):
                    self.visualise.update_game_state('menu')
                elif self.algo1.rect.collidepoint(event.pos):
                    self.algo_choice = self.button_select(self.algo_choice, self.algo1)

                elif self.algo2.rect.collidepoint(event.pos):
                    self.algo_choice = self.button_select(self.algo_choice, self.algo2)

                elif self.algo3.rect.collidepoint(event.pos):
                   self.algo_choice = self.button_select(self.algo_choice, self.algo3)

                elif self.large_maze_btn.rect.collidepoint(event.pos):
                    self.maze_choice = self.button_select(self.maze_choice, self.large_maze_btn)
                
                elif self.medium_maze_btn.rect.collidepoint(event.pos):
                    self.maze_choice = self.button_select(self.maze_choice, self.medium_maze_btn)

                elif self.small_maze_btn.rect.collidepoint(event.pos):
                    self.maze_choice = self.button_select(self.maze_choice, self.small_maze_btn)

                elif self.one_enemy.rect.collidepoint(event.pos):
                    self.enemy_choice = self.button_select(self.enemy_choice, self.one_enemy)
                    self.num_enemys = 1
                    
                elif self.two_enemy.rect.collidepoint(event.pos):
                    self.enemy_choice = self.button_select(self.enemy_choice, self.two_enemy)
                    self.num_enemys = 2
                
                elif self.three_enemy.rect.collidepoint(event.pos):
                    self.enemy_choice = self.button_select(self.enemy_choice, self.three_enemy)
                    self.num_enemys = 3
               
                if go_btn in gui:
                    if go_btn.rect.collidepoint(event.pos):
                        if self.algo_choice == self.algo1:
                            search = 'A*'

                        elif self.algo_choice == self.algo2:
                            search = 'MinMax'
                
                        else:
                            search = 'Expectimax'
                        game = IGame(search, self.maze_choice.get_text(), self.visualise, self.maze, self.num_enemys)
                        game.draw()

                gui.empty()
        
        return gui