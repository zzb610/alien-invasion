import pygame


class Ship():
    """
    Ship class
    """

    def __init__(self, ai_settings, screen):
        """
        init ship and set its position
        """
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # set ship in the center of the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # moving flag
        self.moving_right = False
        self.moving_left = False

        # position
        self.center = float(self.rect.centerx)

    def update(self):
        """
        moving ship, change ceneter x
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """
        draw the ship image
        """
        self.screen.blit(self.image, self.rect)
