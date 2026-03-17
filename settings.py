class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize and adjust the game's static settings."""

        # Screen settings
        self.default_width = 1600
        self.default_height = 900
        self.screen_width = self.default_width
        self.screen_height = self.default_height
        self.bg_color = (30, 130, 210) # it's blue

        # Ship settings
        self.ship_type = 'images/ship1_yellow_small.bmp'

        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 6
        self.bullet_color = (250, 60, 60)
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 10
        
        # Scoring settings
        self.alien_points = 50
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
    
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 8
        self.bullet_speed = 10
        self.alien_speed = 1.0
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
