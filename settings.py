class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize and adjust the game's settings."""
        # Screen settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (30, 130, 210) # it's blue
        # Ship settings
        self.ship_type = 'images/ship1_yellow.bmp'
        self.ship_speed = 2.5
