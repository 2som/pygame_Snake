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
    "colors": {
        "red": (255, 0, 0),
        "blue": (0, 0, 255),
        "green": (0, 255, 0),
        "yellow": (240, 230, 0),
        "grey": (210, 210, 210),
        "orange": (250, 150, 25)
    }
}
