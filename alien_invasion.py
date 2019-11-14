import sys
import pygame
from settings import Settings
from ship import Ship
from flash import Flash
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
    while(True):
        gf.check_events(ship)
        ship.update()
        gf.update_sreen(ai_settings, screen, flash, ship)


if __name__ == "__main__":
    run_game()
