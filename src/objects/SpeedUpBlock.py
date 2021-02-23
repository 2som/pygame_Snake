from src.objects.Block import Block

class SpeedUpBlock(Block):
    def __init__(self, blockConfig, x=0, y=0):
        super().__init__(blockConfig, x, y)
        self.color = blockConfig.get("colors").get("blue")

    def __eq__(self, object):
        if not isinstance(object, SpeedUpBlock):
            return False
        return self.rect.centerx == object.rect.centerx and self.rect.centery == object.rect.centery
        