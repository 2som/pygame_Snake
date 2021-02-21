from src.objects.Block import Block

class MovableBlock(Block):
    def __init__(self, blockConfig, x, y):
        super().__init__(blockConfig, x, y)
        self.prev_x = 0
        self.prev_y = 0

    def update_position(self, x, y):
        if not all(
            map(lambda x: isinstance(x, int), [x, y])):
            raise TypeError
        
        self.save_previous_position()

        self.rect.centerx = x
        self.rect.centery = y
    
    def save_previous_position(self):
        self.prev_x = self.rect.centerx 
        self.prev_y = self.rect.centery

