import sys
import pygame


def check_events(ai_settings, screen, basket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, basket)
        elif event.type == pygame.KEYUP:
            basket.moving = []


def check_keydown_events(event, ai_settings, basket):
    if event.key == pygame.K_RIGHT:
        basket.moving.append('R')
    elif event.key == pygame.K_LEFT:
        basket.moving.append('L')
    elif event.key == pygame.K_q:
        sys.exit()


def update_screen(ai_settings, screen, basket):
    screen.fill(ai_settings.bg_color)

    basket.draw_basket()

    pygame.display.flip()
