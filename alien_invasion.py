import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from flash import Flash
from bullet import Bullet
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(ai_settings, screen)
    # create a flash
    flash = Flash(screen)
    # create a group of bullet
    bullets = Group()
    # crete a group of alien
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while(True):
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.update_sreen(ai_settings, screen, flash, ship, aliens, bullets)


if __name__ == "__main__":
    run_game()
