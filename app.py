import pygame, sys

from Config import Config
from src.objects.Snake import Snake

class App:
    def __init__(self):
        pygame.init()
        self.SETTINGS = Config()

        if not self.SETTINGS.screen_width:
            self.SETTINGS.screen_width = 1200
        
        if not self.SETTINGS.screen_height:
            self.SETTINGS.screen_height = 800

        self.screen = pygame.display.set_mode(
            (self.SETTINGS.screen_width, self.SETTINGS.screen_height)
        )

        pygame.display.set_caption("Snake")

        self.snake = Snake(self.screen)
        self.snake.initialize_position()

    def run(self):
        self.snake.display()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:             
                    if event.key == pygame.K_RIGHT:
                        self.snake.set_moving_direction('right')
                    elif event.key == pygame.K_LEFT:
                        self.snake.set_moving_direction('left')
                    elif event.key == pygame.K_UP:
                        self.snake.set_moving_direction('up')
                    elif event.key == pygame.K_DOWN:
                        self.snake.set_moving_direction('down')
            
            self.snake.move()
            pygame.display.flip()

    
    def check_events(self):
        pass

    def update_screen(self):
        pass


App().run()