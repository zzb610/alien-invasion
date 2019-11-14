import pygame


class Flash():
    """
    flash image in the center
    """

    def __init__(self, screen):
        
        self.screen = screen

        # load image
        self.image = pygame.image.load('images/flash.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # set position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
    
    def blitme(self):
        """
        draw the image
        """
        self.screen.blit(self.image, self.rect)

