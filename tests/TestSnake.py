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
        assert snake.head.rect.centery == 99 and snake.head.rect.centerx == 100

    def test_snake_moves_down_correctly(self):
        snake = self.there_is_snake_object()
        
        snake.set_moving_direction('down')
        snake.move()
        assert snake.head.rect.centery == 101 and snake.head.rect.centerx == 100

    def test_snake_moves_left_correctly(self):
        snake = self.there_is_snake_object()
        
        snake.set_moving_direction('left')
        snake.move()
        assert snake.head.rect.centery == 100 and snake.head.rect.centerx == 99

    def test_snake_moves_right_correctly(self):
        snake = self.there_is_snake_object()
        
        snake.set_moving_direction('right')
        snake.move()
        assert snake.head.rect.centery == 100 and snake.head.rect.centerx == 101

    def snake_enlarges_his_body(self):
        snake = self.there_is_snake_object()

        additional_part = MovableBlock(mocks.blockConfig, 99, 100)
        snake.enlarge(additional_part)

        assert len(snake.body) == 2
        assert additional_part in self.body

    def test_snake_updates_body_position(self):
        snake = self.there_is_snake_object()
        additional_part = MovableBlock(mocks.blockConfig, 99, 100)
        
        snake.enlarge(additional_part)
        snake.move()
        snake.update_body()
        
        assert additional_part.rect.centerx == 100
    
    def test_snake_handles_updating_larger_body(self):
        snake = self.there_is_snake_object()
        additional_parts = [MovableBlock(mocks.blockConfig, 100, 101), 
                            MovableBlock(mocks.blockConfig, 100, 102), 
                            MovableBlock(mocks.blockConfig, 100, 103), 
                            MovableBlock(mocks.blockConfig, 99, 103)]
                            
        snake.body = snake.body + additional_parts
        snake.moving_direction = 'up'
        snake.move()

        assert additional_parts[0].rect.centerx == 100 and additional_parts[0].rect.centery == 100
        assert additional_parts[1].rect.centerx == 100 and additional_parts[1].rect.centery == 101
        assert additional_parts[2].rect.centerx == 100 and additional_parts[2].rect.centery == 102
        assert additional_parts[3].rect.centerx == 100 and additional_parts[3].rect.centery == 103


    def there_is_snake_object(self):
        return Snake(mocks.ScreenFixture(),  MovableBlock(mocks.blockConfig, 100, 100))