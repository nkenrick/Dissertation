from GUI import *
from button import Button

'''
Gui for the end of a visualisation. Displays whether an agent was successful or not, the time they took and how many steps they took. 
'''

class EndgameUI(GUI):
    def __init__(self, visualise, size, screen, state, time, steps, maze, learning=False):
        super().__init__(visualise,  size, screen)
        self.state = state 
        self.time = time
        self.steps = steps
        self.maze = maze
        self.size = size
        self.learning = learning

    def draw(self):
        w, h = pygame.display.get_surface().get_size()
        self.size = w
        gui = pygame.sprite.Group()

        if self.drawn == False:
            quit_button = Button(pos=(100, 20), text="QUIT", menu=self)
            quit_w, quit_h = quit_button.get_button_size()
            quit_button.update_pos(self.size - 20- quit_w, 20)
            
            if not self.learning:
                if self.state:
                    state_text = self.font.render("Winner!!!", True, (0, 0, 0))
                else:
                    state_text = self.font.render("Game over!", True, (0, 0, 0))
                state_text_rect = state_text.get_rect(center=(self.rect.w/2, 50))
                self.screen.blit(state_text, state_text_rect)

                test1 = "Time taken: "+ str(round(self.time, 3))
                time_text = self.font.render(test1, True, (0, 0, 0))
                time_text_rect = time_text.get_rect(center=(self.rect.w/2, 100))
                self.screen.blit(time_text, time_text_rect)
                
                maze_save = self.font.render('Save this maze?', True, (0, 0, 0))
                maze_save_rect = maze_save.get_rect(center=(self.rect.w/2, 180))
                self.screen.blit(maze_save, maze_save_rect)

                save_maze = Button(pos=(100, 20), text="Yes", menu=self)
                save_maze_w, save_maze_h = save_maze.get_button_size()
                save_maze.update_pos(self.rect.w/2 - save_maze_w/2, 220)

                dont_save = Button(pos=(100, 20), text="No", menu=self)
                dont_save_w, dont_save_h = dont_save.get_button_size()
                dont_save.update_pos(self.rect.w/2 - dont_save_w/2,280)
                gui.add(save_maze, dont_save)

            else:
                save_maze = None
                dont_save = None
                main_button = Button(pos=(20, 20), text="Main Menu", menu=self)

                test1 = "Optimal number of steps: 34 "
                time_text = self.font.render(test1, True, (0, 0, 0))
                time_text_rect = time_text.get_rect(center=(self.rect.w/2, 100))
                self.screen.blit(time_text, time_text_rect)

                episode = "Episodes ran: " + str(self.learning)
                episode_text = self.font.render(episode, True, (0, 0, 0))
                episode_text_rect = episode_text.get_rect(center=(self.rect.w/2, 200))
                self.screen.blit(episode_text, episode_text_rect)

                gui.add(main_button)

            test2 = "Steps taken: " + str(self.steps)
            steps_text = self.font.render(test2, True, (0, 0, 0))
            steps_text_rect = steps_text.get_rect(center=(self.rect.w/2, 140))
            self.screen.blit(steps_text, steps_text_rect)

        gui.add(quit_button)
            

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if quit_button.rect.collidepoint(event.pos):
                    self.exit()

                if save_maze in gui and save_maze.rect.collidepoint(event.pos):
                    self.visualise.update_game_state('algorithm_select')
                    self.visualise.save_maze(self.maze)
                
                elif dont_save in gui and dont_save.rect.collidepoint(event.pos):
                    self.visualise.update_game_state('algorithm_select')
                    self.visualise.save_maze(None)  

                elif main_button in gui and main_button.rect.collidepoint(event.pos):
                    self.visualise.update_game_state('menu')
        return gui