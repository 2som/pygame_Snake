class ScreenFixture:
    def __init__(self):
        self.rect = RectFixture(100,100)
    def get_rect(self):
        self.rect
        

class RectFixture:
    def __init__(self, x, y):
        self.centerx = x
        self.centery = y