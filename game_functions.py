import sys
import pygame


def check_keydown_events(event, ship):
    """
    response to key down
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_event(event, ship):
    """
    response to key up
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """
    response to button and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_sreen(ai_settings, screen, flash, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    flash.blitme()
    # draw whole picture
    pygame.display.flip()
