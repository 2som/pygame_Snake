import pygame

class Snake:
    def __init__(self, screen, movableBlock):
        self.screen = screen
        self.head = movableBlock
        self.moving_direction = 'left'
        self.body = [self.head]

    def set_moving_direction(self, direction):
        if not isinstance(direction, str):
            return
        elif direction not in ['left', 'right', 'up', 'down']:
            return 

        self.moving_direction = direction
        
    def move(self):
        self.save_previous_position()
      
        if self.moving_direction == 'left':
            self._move_left()
        elif self.moving_direction == 'right':
            self._move_right()
        elif self.moving_direction == 'down':
            self._move_down()
        elif self.moving_direction == 'up':
            self._move_up()
        else:
            return

        self.update_body()

    def save_previous_position(self):
        self.head.save_previous_position()
    
    def update_body(self):
        for i in range(0, len(self.body) - 1):
            current_block = self.body[i]
            next_block = self.body[i + 1]
            next_block.update_position(current_block.prev_x, current_block.prev_y)
  
    def display(self):
        for i in range(0, len(self.body)):
            pygame.draw.rect(self.screen, (255, 0, 0), self.body[i].rect)

    def enlarge(self, block):
        self.body.append(block)
        print(self.body)
        
    def _move_up(self):
        self.head.rect.centery -= 1

    def _move_down(self):
        self.head.rect.centery += 1

    def _move_left(self):
        self.head.rect.centerx -= 1

    def _move_right(self):
        self.head.rect.centerx += 1