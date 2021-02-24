import random

from src.objects.Block import Block

class BlockSpawner:
    def __init__(self, settings):
        self.rules = {
            "max_x": settings.board_width + settings.board_offset,
            "max_y": settings.board_height + settings.board_offset,
            "offset": settings.board_offset
        }
        self.last_spawned_positions = []
        self.block_config = settings.block_config

    def spawn_block(self, block):
        if not isinstance(block, Block):
            raise TypeError("Given block is not type of Block")
        
        x, y = self._generate_random_position()
        
        block.set_position(x, y)

    def _generate_random_position(self):
        x, y = self._get_random_coords()
        while not self._check_if_random_coords_are_random_enough(x, y):
            x, y = self._get_random_coords()
        
        if (len(self.last_spawned_positions) >= 3):
            self.last_spawned_positions.pop(0)

        self.last_spawned_positions.append({ "x": x, "y": y })

        return [x, y]

    def _get_random_coords(self):
        x = random.randint(
            self.rules.get("offset") + self.block_config.get("width", 50), 
            self.rules.get("max_x", 1200) - self.block_config.get("width", 50))
        y = random.randint(
            self.rules.get("offset") + self.block_config.get("width", 50), 
            self.rules.get("max_y", 800) - self.block_config.get("width", 50))
        return [x, y]

    def _check_if_random_coords_are_random_enough(self, x, y):
        if not self.last_spawned_positions:
            return True
        
        for coords in self.last_spawned_positions:
            if (abs(coords.get("x") - x) + (abs(coords.get("y") - y)) <= 200):
                return False
        else:
            return True