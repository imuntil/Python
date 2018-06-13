import pygame
from settings import Settings
from basket import Basket
from ball import Ball
import fns


def run():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption('Basket Ball')

    basket = Basket(ai_settings, screen)
    ball = Ball(ai_settings, screen)

    while True:
        fns.check_events(ai_settings, screen, basket)
        if ai_settings.changes >= 0:
            basket.update()
            fns.update_ball(ai_settings, screen, ball, basket)
        fns.update_screen(ai_settings, screen, basket, ball)


run()
