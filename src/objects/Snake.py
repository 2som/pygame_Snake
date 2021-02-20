import pygame

class Snake:
    def __init__(self, screen, rect):
        self.screen = screen
        self.rect = rect
        self.moving_direction = 'left'

    def set_moving_direction(self, direction):
        if not isinstance(direction, str):
            return
        elif direction not in ['left', 'right', 'up', 'down']:
            return 

        self.moving_direction = direction
        
    def move(self):
        if self.moving_direction == 'left':
            self._move_left()
        elif self.moving_direction == 'right':
            self._move_right()
        elif self.moving_direction == 'down':
            self._move_down()
        elif self.moving_direction == 'up':
            self._move_up()
        
    def display(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
        
    def _move_up(self):
        self.rect.centery -= 1

    def _move_down(self):
        self.rect.centery += 1

    def _move_left(self):
        self.rect.centerx -= 1

    def _move_right(self):
        self.rect.centerx += 1