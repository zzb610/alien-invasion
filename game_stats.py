class GameStats():
    """
    Track game statistics
    """

    def __init__(self, ai_settings):
        """
        init statistics
        """
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """
        reset statistics
        """
        self.ship_left = self.ai_settings.ship_limit
