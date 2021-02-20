import pygame

class Block:
    def __init__(self, blockConfig, x=0, y=0):
        self.width = blockConfig.get('width', 50)
        self.height = blockConfig.get('height', 50)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
