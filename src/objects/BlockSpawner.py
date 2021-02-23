import pygame
import random

class BlockSpawner:
    def __init__(self, screen, blockConfig):
        self.rules = {
            "max_x": pygame.display.get_surface().get_width(),
            "max_y": pygame.display.get_surface().get_height()
        }
        self.last_spawned_positions = []
        self.screen = screen
        self.blockConfig = blockConfig

    
    def spawn_block(self, block):
        x, y = self._generate_random_position()
        block.set_position(x, y)
        pygame.draw.rect(self.screen, block.color, block.rect)

    
    def _generate_random_position(self):
        x, y = self._get_random_coords()
        while not self._check_if_random_coords_are_random_enough(x, y):
            x, y = self._get_random_coords()
        
        if (len(self.last_spawned_positions) >= 3):
            self.last_spawned_positions.pop(0)

        self.last_spawned_positions.append({ "x": x, "y": y })

        return [x, y]

    def _get_random_coords(self):
        x = random.randint(0, self.rules.get("max_x", 1200) - self.blockConfig.get("width", 50) / 2)
        y = random.randint(0, self.rules.get("max_y", 800) - self.blockConfig.get("width", 50) / 2)
        return [x, y]

    def _check_if_random_coords_are_random_enough(self, x, y):
        if not self.last_spawned_positions:
            return True
        
        for coords in self.last_spawned_positions:
            if (abs(coords.get("x") - x) + (abs(coords.get("y") - y)) <= 200):
                return False
        else:
            return True