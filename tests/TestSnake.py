import tests.mocks as mocks
from src.objects.Snake import Snake
from src.objects.MovableBlock import MovableBlock


class TestSnake:
    def test_snake_initial_direction_is_left(self):
        snake = self.there_is_snake_object()

        assert snake.moving_direction == 'left'

    def test_snake_accepts_moving_direction(self):
        snake = self.there_is_snake_object()
        
        snake.set_moving_direction('left')
        
        assert snake.moving_direction == 'left'

    def test_snake_invalid_direction(self):
        snake = self.there_is_snake_object()
        
        snake.set_moving_direction(123)
        snake.set_moving_direction('d')
        
        assert snake.moving_direction == 'left'

    def test_snake_remembers_last_direction_when_invalid_direction_given(self):
        snake = self.there_is_snake_object()
        
        snake.set_moving_direction('up')
        snake.set_moving_direction(123)

        assert snake.moving_direction == 'up'

    def test_snake_moves_up_correctly(self):
        snake = self.there_is_snake_object()
        
        snake.set_moving_direction('up')
        snake.move()
        assert snake.head.rect.centery == 50 and snake.head.rect.centerx == 100

    def test_snake_moves_down_correctly(self):
        snake = self.there_is_snake_object()
        
        snake.set_moving_direction('down')
        snake.move()
        assert snake.head.rect.centery == 150 and snake.head.rect.centerx == 100

    def test_snake_moves_left_correctly(self):
        snake = self.there_is_snake_object()
        
        snake.set_moving_direction('left')
        snake.move()
        assert snake.head.rect.centery == 100 and snake.head.rect.centerx == 50

    def test_snake_moves_right_correctly(self):
        snake = self.there_is_snake_object()
        snake.set_moving_direction('up') 
        snake.set_moving_direction('right')
        snake.move()
        assert snake.head.rect.centery == 100 and snake.head.rect.centerx == 150

    def snake_enlarges_his_body(self):
        snake = self.there_is_snake_object()

        additional_part = MovableBlock(mocks.blockConfig, 99, 100)
        snake.eat(additional_part)

        assert len(snake.body) == 2
        assert additional_part in self.body

    def test_snake_updates_body_position(self):
        snake = self.there_is_snake_object()
        additional_part = MovableBlock(mocks.blockConfig, 50, 100)
        
        snake.eat(additional_part)
        snake.move()
        snake.update_body()
        
        assert additional_part.rect.centerx == 100
    
    def test_snake_handles_updating_larger_body(self):
        snake = self.there_is_snake_object()
        additional_parts = [MovableBlock(mocks.blockConfig, 100, 150), 
                            MovableBlock(mocks.blockConfig, 100, 200), 
                            MovableBlock(mocks.blockConfig, 100, 250), 
                            MovableBlock(mocks.blockConfig, 50, 250)]
                            
        snake.body = snake.body + additional_parts
        snake.moving_direction = 'up'
        snake.move()

        assert additional_parts[0].rect.centerx == 100 and additional_parts[0].rect.centery == 100
        assert additional_parts[1].rect.centerx == 100 and additional_parts[1].rect.centery == 150
        assert additional_parts[2].rect.centerx == 100 and additional_parts[2].rect.centery == 200
        assert additional_parts[3].rect.centerx == 100 and additional_parts[3].rect.centery == 250


    def test_snake_cannot_turn_in_opposite_direction_y_axis(self):
        snake = self.there_is_snake_object()
        snake.set_moving_direction('down')
        snake.set_moving_direction('up')

        assert snake.get_moving_direction() == 'down'

    def test_snake_cannot_turn_in_opposite_direction_x_axis(self):
        snake = self.there_is_snake_object()
        snake.set_moving_direction('left')
        snake.set_moving_direction('right')

        assert snake.get_moving_direction() == 'left'

    def test_snake_slows_down(self):
        snake = self.there_is_snake_object()
        snake.speed = 50

        snake.slow_down()

        assert snake.speed == 30 and snake.state == 'slowed'

    def test_snake_is_not_slowing_down_when_already_slowed_down(self):
        snake = self.there_is_snake_object()
        snake.speed = 50
        snake.state = 'accelerated'

        snake.slow_down()

        assert snake.speed == 50 and snake.state == 'slowed'

    def test_snake_speeds_up(self):
        snake = self.there_is_snake_object()
        snake.speed = 50

        snake.speed_up()

        assert snake.speed == 70 and snake.state == 'accelerated'

    def test_snake_is_not_speeding_up_when_already_speeded_up(self):
        snake = self.there_is_snake_object()
        snake.speed = 50
        snake.state = 'accelerated'

        snake.speed_up()

        assert snake.speed == 50 and snake.state == 'accelerated'


    def there_is_snake_object(self):
        return Snake(mocks.ScreenFixture(),  MovableBlock(mocks.blockConfig, 100, 100), 50)