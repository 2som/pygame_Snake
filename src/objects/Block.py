import pygame

class Block:
    def __init__(self, blockConfig, x=0, y=0):
        self.width = blockConfig.get('width', 50)
        self.height = blockConfig.get('height', 50)
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.rect.centerx = x
        self.rect.centery = y
