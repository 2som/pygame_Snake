import pygame

class Block:
    def __init__(self, blockConfig, x=0, y=0):
        self.width = blockConfig.get('width', 10)
        self.height = blockConfig.get('height', 10)
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.rect.centerx = x
        self.rect.centery = y
        self.color = blockConfig.get("colors").get('grey')

    def set_position(self, x, y):
        if not all(
            map(lambda x: isinstance(x, int), [x, y])):
            raise TypeError

        self.rect.centerx = x
        self.rect.centery = y
    
    def __eq__(self, object):
        if not isinstance(object, Block):
            return False
        return self.rect.centerx == object.rect.centerx and self.rect.centery == object.rect.centery
        