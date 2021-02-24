from src.objects.Block import Block
from src.objects.MovableBlock import MovableBlock


class BlockFacade:
    def __init__(self, blockConfig):
        self.blocks = []
        self.blockConfig = blockConfig
    
    def create_block(self, x=0, y=0):
        return Block(self.blockConfig, x, y)
    
    def create_movable_block(self, x=0, y=0):
        return MovableBlock(self.blockConfig, x, y)
        