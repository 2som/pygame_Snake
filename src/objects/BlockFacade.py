from src.objects.SpeedUpBlock import SpeedUpBlock
from src.objects.Block import Block
from src.objects.MovableBlock import MovableBlock
from src.objects.SlowDownBlock import SlowDownBlock


class BlockFacade:
    def __init__(self, blockConfig):
        self.blocks = []
        self.blockConfig = blockConfig
    
    def createBlock(self, x=0, y=0):
        return Block(self.blockConfig, x, y)
    
    def createMovableBlock(self, x=0, y=0):
        return MovableBlock(self.blockConfig, x, y)

    def createSlowDownBlock(self, x=0, y=0):
        return SlowDownBlock(self.blockConfig, x, y)

    def createSpeedUpBlock(self, x=0, y=0):
        return SpeedUpBlock(self.blockConfig, x, y)
    
    
        