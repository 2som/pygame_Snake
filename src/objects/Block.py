import pygame

class Block:
    def __init__(self, screen, x, y, width, height, color):
        self.rect = pygame.Rect(
            self.screen_rect.centerx, 
            self.screen_rect.centery,
            50,
            50
        )
