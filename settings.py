class Settings():
    """
    all game settings
    """

    def __init__(self):
        # screen settings
        self.screen_width = 1000
        self.screen_height = 900
        self.bg_color = (66, 133, 244)

        # ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20
        self.fleet_direction = 1  # 1 right -1 left
