from src.objects.MovableBlock import MovableBlock
from src.objects.SlowDownBlock import SlowDownBlock
from src.objects.SpeedUpBlock import SpeedUpBlock

class Snake:
    def __init__(self, screen, movableBlock, speed):
        self.screen = screen
        self.head = movableBlock
        self.moving_direction = 'left'
        self.body = [self.head]
        self.speed = speed
        self.state = 'normal'

    def set_moving_direction(self, direction):
        if not isinstance(direction, str):
            return
        elif direction not in ['left', 'right', 'up', 'down']:
            return 
        
        if not self.can_turn(direction):
            return

        self.moving_direction = direction

    def get_moving_direction(self):
        return self.moving_direction
        
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
       
    def eat(self, block):
        if isinstance(block, MovableBlock):
            self.body.append(block)
            return
        if isinstance(block, SlowDownBlock):
            self.slow_down()
            return
        if isinstance(block, SpeedUpBlock):
            self.speed_up()
            return
        
        raise TypeError("I don't know how to eat that.")
        
    def eats_himself(self):
        for rect in self.body[1:]:
            if rect.rect.colliderect(self.head):
                return True
        return False

    def position_new_part(self, block):
        last_part = self.body[-1]
        block.update_position(last_part.prev_x, last_part.prev_y)

    def can_turn(self, direction):
        if direction == 'right' and self.moving_direction == 'left':
            return False

        if direction == 'left' and self.moving_direction == 'right':
            return False

        if direction == 'down' and self.moving_direction == 'up':
            return False

        if direction == 'up' and self.moving_direction == 'down':
            return False

        return True

    def speed_up(self):
        if self.state == 'accelerated':
            return

        if self.state == 'slowed':
            self.state = 'normal'
            self.speed += 50
            return
        
        if self.state == 'normal':
            self.state = 'accelerated'
            self.speed += 50
            return
        

    def slow_down(self):
        if self.state == 'slowed':
            return

        if self.state == 'accelerated':
            self.state = 'normal'
            self.speed -= 20
            return
        
        if self.state == 'normal':
            self.state = 'slowed'
            self.speed -= 20
            return

    def reset_state(self):
        if self.state == 'slowed':
            self.speed += 20
        elif self.state == 'accelerated':
            self.speed -= 20
        self.state == 'normal'

    def _move_up(self):
        self.head.rect.centery -= self.speed

    def _move_down(self):
        self.head.rect.centery += self.speed

    def _move_left(self):
        self.head.rect.centerx -= self.speed

    def _move_right(self):
        self.head.rect.centerx += self.speed