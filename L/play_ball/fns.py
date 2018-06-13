import sys
import pygame
from time import sleep


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


def update_screen(ai_settings, screen, basket, ball):
    screen.fill(ai_settings.bg_color)

    ball.draw_ball()
    basket.draw_basket()

    pygame.display.flip()


def update_ball(ai_settings, screen, ball, basket):
    ball.update()
    check_basket_meet_ball(basket, ball)
    check_ball_to_bottom(ai_settings, ball)


def check_basket_meet_ball(basket, ball):
    if basket.rect.colliderect(ball.rect):
        sleep(.5)
        ball.reset_ball()


def check_ball_to_bottom(ai_settings, ball):
    if ball.rect.bottom >= ai_settings.screen_height:
        ai_settings.changes -= 1
        sleep(.5)
        ball.reset_ball()
