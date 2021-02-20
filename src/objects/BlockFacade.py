from src.objects.Block import Block

class BlockFacade:
    def __init__(self, blockConfig):
        self.blocks = []
        self.blockConfig = blockConfig
    
    def createBlock(self, x=0, y=0):
        return Block(self.blockConfig, x, y).rect
        

    def createBlockAtRandomPosition(self):
        pass