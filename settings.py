class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize and adjust the game's settings."""

        # Screen settings
        self.default_width = 1600
        self.default_height = 900
        self.screen_width = self.default_width
        self.screen_height = self.default_height
        self.bg_color = (30, 130, 210) # it's blue

        # Ship settings
        self.ship_type = 'images/ship1_yellow.bmp'
        self.ship_speed = 5

        # Bullet settings
        self.bullet_speed = 6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 60, 60)
        self.bullets_allowed = 6

        # Alien settings
        self.alien_speed = 1.0
