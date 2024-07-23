class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 1920
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)

        #Ship Settings
        self.ship_limit = 3

        #Bullet Settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Alien Settings
        self.fleet_drop_speed = 0.5

        #How quickly the game speed ups
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5

        #fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        def increase_speed(self):
            """Increase speed settings."""
            self.ship_speed *= self.speedup_scale
            self.bullet_speed *= self.speedup_scale
            self.alien_speed *= self.speedup_scale