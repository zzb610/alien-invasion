import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    Aline
    """

    def __init__(self, ai_settings, screen):
        super().__init__()

        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """
        draw alien
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        move alien
        """
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x
