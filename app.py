import pygame, sys

from Config import Config
from src.objects.BlockSpawner import BlockSpawner
from src.objects.Snake import Snake
from src.objects.BlockFacade import BlockFacade
from src.objects.Board import Board
from src.components.Button import Button

class App:
    def __init__(self):
        self.SETTINGS = None
        self.rects = []
        self.current_spawned_rect = None
        self.screen = None
        self.spawner = None
        self.quit_button = None
        self.try_again_btn = None
        self.block_facade = None
        self.state = 1
        self.score = 0

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
        self.board = Board(
            self.SETTINGS.block_config.get("colors").get("very_dark_green"),
            self.SETTINGS.board_offset,
            self.SETTINGS.board_offset,
            self.SETTINGS.board_width,
            self.SETTINGS.board_height
        )

        self.block_facade = BlockFacade(self.SETTINGS.block_config)
        
        self.snake = Snake(self.screen, self.block_facade.create_movable_block(
            self.screen.get_rect().centerx,
            self.screen.get_rect().centery
        ), self.SETTINGS.snake_speed)

        self.rects.append(self.snake)
        
        self.spawner = BlockSpawner(self.SETTINGS)
        self.try_again_btn = Button(
                    self.SETTINGS.block_config.get("colors").get("green"), 
                    self.SETTINGS.screen_width / 2 - 200,
                    self.SETTINGS.screen_height / 2 - 50,
                    100,
                    50,
                    'try again'
                )
        self.quit_button = Button(
            self.SETTINGS.block_config.get("colors").get("red"), 
            self.SETTINGS.screen_width / 2 + 50,
            self.SETTINGS.screen_height / 2 - 50,
            100, 
            50,
            'quit'
        )
       
    def run(self):
        clock = pygame.time.Clock()
        time = 0
        while True:
            if self.state == 1:
                time += clock.get_time()
                score_text_font = pygame.font.SysFont('Arial', 30)
                text_surface = score_text_font.render(f'score: {self.score}', False, self.SETTINGS.block_config.get("colors").get("white"))
               
                if time >= 100:
                    self.check_events(pygame.event.get())
                    self.check_collisions()
                    self.update_screen()
                    time = 0
            else:
                self.screen.fill((0, 0, 0))
                self.try_again_btn.draw(self.screen)
                self.quit_button.draw(self.screen)
                
                self.check_events(pygame.event.get())
            
            self.screen.blit(text_surface,(0,0))
            pygame.display.flip()
            
            clock.tick(100)
                
    def check_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:             
                if event.key == pygame.K_RIGHT:
                    self.snake_is_moving('right')
                elif event.key == pygame.K_LEFT:
                    self.snake_is_moving('left')
                elif event.key == pygame.K_UP:
                    self.snake_is_moving('up')
                elif event.key == pygame.K_DOWN:
                    self.snake_is_moving('down')
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.try_again_btn.is_hovered(pygame.mouse.get_pos()):
                    self.restart()
                elif self.quit_button.is_hovered(pygame.mouse.get_pos()):
                    sys.exit()

    def snake_is_moving(self, direction):
        self.snake.set_moving_direction(direction)
    
    def restart(self):
        self.rects = []
        self.current_spawned_rect = None
        self.state = 1
        self.score = 0
        self.initialize_objects()
    
    def check_collisions(self):
        if self.snake_eats_himself():
            self.state = 0

        if self.snake_is_outside_of_board():
            self.state = 0

        if self.snake_found_food():
            self.snake_eats()
        
    def snake_eats_himself(self):
        return self.snake.eats_himself()

    def snake_is_outside_of_board(self):
        return (self.snake.head.rect.x > self.SETTINGS.board_width + self.SETTINGS.board_offset or 
                self.snake.head.rect.x < self.SETTINGS.board_offset or 
                self.snake.head.rect.y > self.SETTINGS.board_height + self.SETTINGS.board_offset or 
                self.snake.head.rect.y < self.SETTINGS.board_offset)

    def snake_found_food(self):
        return self.snake.head.rect.colliderect(self.current_spawned_rect.rect)
    
    def snake_eats(self):
        self.remove_rect_from_rects(self.current_spawned_rect)
        new_snake_part = self.block_facade.create_movable_block()
        self.snake.eat(new_snake_part)
        self.rects.append(new_snake_part)
        self.current_spawned_rect = None
        self.score += 1

    def remove_rect_from_rects(self, rect):
        self.rects = list(filter(lambda x: x != rect, self.rects))
    
    def update_screen(self):
        self.screen.fill((0, 0, 0))
        self.board.draw(self.screen)
        
        if not self.current_spawned_rect:
            self.spawn_rect()

        self.update_snake_position()
        
        for rect in self.rects:
            if isinstance(rect, Snake):
                pygame.draw.rect(self.screen, rect.head.color, rect.head)
                continue
          
            pygame.draw.rect(self.screen, rect.color, rect.rect)

    def spawn_rect(self):
        self.current_spawned_rect = self.block_facade.create_block()
        self.spawner.spawn_block(self.current_spawned_rect)
        self.rects.append(self.current_spawned_rect)

    def update_snake_position(self):
        self.snake.move()
    

App().run()