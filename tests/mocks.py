class ScreenFixture:
    def __init__(self):
        self.rect = RectFixture(100,100)
    def get_rect(self):
        self.rect
        

class RectFixture:
    def __init__(self, x, y, width=50, height=50):
        self.centerx = x
        self.centery = y
        self.width = width
        self.height = height


blockConfig = {
    "width": 50,
    "height": 50,
    "color1": (0, 255, 0),
    "color2": (0, 0, 255),
}
