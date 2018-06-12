import pygame
from settings import Settings
from basket import Basket
import fns


def run():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Basket Ball')

    basket = Basket(ai_settings, screen)

    while True:
        fns.check_events(ai_settings, screen, basket)
        basket.update()
        fns.update_screen(ai_settings, screen, basket)


run()
