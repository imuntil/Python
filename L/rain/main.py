import pygame
from pygame.sprite import Group
from settings import Settings
import fns


def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Rain')

    drips = Group()

    fns.create_fleet(ai_settings, screen, drips)

    while True:
        fns.check_events(ai_settings, screen)

        fns.update_drips(ai_settings, drips)
        fns.update_screen(ai_settings, screen, drips)


run_game()
