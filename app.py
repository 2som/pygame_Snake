import pygame, sys

from Config import Config
from src.objects.BlockSpawner import BlockSpawner
from src.objects.Snake import Snake
from src.objects.BlockFacade import BlockFacade

class App:
    def __init__(self):
        self.rects = []
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
        
        self.snake = Snake(self.screen, self.blockFacade.createMovableBlock(
            self.screen.get_rect().centerx,
            self.screen.get_rect().centery
        ), self.SETTINGS.snake_speed)
        
        self.spawner = BlockSpawner(self.screen, self.SETTINGS)
       
    def run(self):
        clock = pygame.time.Clock()
        time = 0
        while True:
            time += clock.get_time()
            if time >= 100:
                self.screen.fill((0, 0, 0))
                self.check_events(pygame.event.get())
                self.update_screen()
                pygame.display.flip()
                time = 0
            clock.tick(120)
             
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
        self.snake.move()
        for rect in self.rects:
            if isinstance(rect, Snake):
                pygame.draw.rect(self.screen, rect.head.color, rect.head)
            else:   
                pygame.draw.rect(self.screen, rect.color, rect.rect)

    def spawn_rect(self):
        pass

App().run()