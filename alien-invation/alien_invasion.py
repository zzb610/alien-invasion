import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from flash import Flash
from bullet import Bullet
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
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
    # create a GameStat
    stats = GameStats(ai_settings)
    # create a play buttom
    play_button = Button(ai_settings, screen, 'Play')
    # create a scoreboard
    sb = Scoreboard(ai_settings, screen, stats)

    while(True):
        gf.check_events(ai_settings, screen, stats, sb,
                        play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats,
                              sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb,
                             screen, ship, aliens, bullets)
        gf.update_sreen(ai_settings, stats, sb, screen, flash, ship,
                        aliens, bullets, play_button)


if __name__ == "__main__":
    run_game()
