class Config:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.board_width = 1000
        self.board_height = 600
        self.board_offset = 100
        self.block_config = {
            "width": 25,
            "height": 25,
            "colors": {
                "red": (255, 0, 0),
                "blue": (0, 0, 255),
                "green": (0, 255, 0),
                "yellow": (240, 230, 0),
                "grey": (210, 210, 210),
                "orange": (250, 150, 25),
                "very_dark_green": (44, 54, 45),
                "white": (255, 255, 255)
            }
        }
        self.snake_speed = 25
        