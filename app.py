import pygame, sys

from Config import Config
from src.objects.Snake import Snake
from src.objects.BlockFacade import BlockFacade

class App:
    def __init__(self):
        self.setup_settings_and_screen()
        self.initialize_objects()

    def setup_settings_and_screen(self):
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

    def initialize_objects(self):
        self.blockFacade = BlockFacade(self.SETTINGS.blockConfig)
        
        self.snake = Snake(self.screen, self.blockFacade.createBlock(
            self.screen.get_rect().centerx,
            self.screen.get_rect().centery
        ))

    def run(self):
        self.screen.fill((0, 0, 0))
        self.snake.display()
        while True:
            self.screen.fill((0, 0, 0))
            self.check_events(pygame.event.get())
            self.snake.move()
            self.snake.display()
            pygame.display.flip()

    
    def check_events(self, events):
        for event in events:
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
        
    def update_screen(self):
        pass


App().run()