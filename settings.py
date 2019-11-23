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

        # enhance
        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        # score
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        """
        init the difficulty of the game
        """
        self.ship_speed_factor = 1.2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1  # 1 right -1 left

    def increase_speed(self):
        """
        increase game speed
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)
