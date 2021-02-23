class Config:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.blockConfig = {
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
        self.snake_speed = 50
        