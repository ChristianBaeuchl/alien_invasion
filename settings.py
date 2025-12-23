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
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 7
        self.bullet_height = 7
        self.bullet_color = (250, 60, 60)
        self.bullets_allowed = 8

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
