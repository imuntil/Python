import sys
import pygame


def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def check_keydown_events(event, rocket):
    print(event.key)
    if event.key == pygame.K_RIGHT:
        rocket.move.append('RIGHT')
    elif event.key == pygame.K_LEFT:
        rocket.move.append('LEFT')
    elif event.key == pygame.K_UP:
        rocket.move.append('UP')
    elif event.key == pygame.K_DOWN:
        rocket.move.append('DOWN')


def check_keyup_events(event, rocket):
    rocket.move = []


def update_screen(ai_settings, screen, rocket):
    screen.fill(ai_settings.bg_color)
    rocket.blitme()

    pygame.display.flip()