import os

class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score schould never be reset.
        self.high_score = self.read_high_score()
        
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def read_high_score(self):
        file_name = "highscore.txt"

        # Try to read the existing high score
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                content = f.read().strip()
                if content:
                    return int(content)
        else:
            return 0