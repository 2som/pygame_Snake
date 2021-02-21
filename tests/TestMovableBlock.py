import tests.mocks as mocks
from src.objects.MovableBlock import MovableBlock

class TestMovableBlock:
    def test_update_position(self):
        block = MovableBlock(mocks.blockConfig, 100, 100)

        block.update_position(99, 100)

        assert block.prev_x == 100
        assert block.prev_y == 100
        assert block.rect.centerx == 99
