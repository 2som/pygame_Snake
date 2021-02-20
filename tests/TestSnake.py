import pytest

import tests.mocks as mocks
from src.objects.Snake import Snake


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
        assert snake.rect.centery == 99 and snake.rect.centerx == 100

    def test_snake_moves_down_correctly(self):
        snake = self.there_is_snake_object()
        
        snake.set_moving_direction('down')
        snake.move()
        assert snake.rect.centery == 101 and snake.rect.centerx == 100

    def test_snake_moves_left_correctly(self):
        snake = self.there_is_snake_object()
        
        snake.set_moving_direction('left')
        snake.move()
        assert snake.rect.centery == 100 and snake.rect.centerx == 99

    def test_snake_moves_right_correctly(self):
        snake = self.there_is_snake_object()
        
        snake.set_moving_direction('right')
        snake.move()
        assert snake.rect.centery == 100 and snake.rect.centerx == 101

    def there_is_snake_object(self):
        return Snake(mocks.ScreenFixture(), mocks.RectFixture(100, 100))