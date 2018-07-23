class Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self) -> object:
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (200, 200, 240)

        # Ship settings
        self.ship_speed_factor = 1.5
