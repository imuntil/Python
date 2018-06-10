import sys

import pygame
from drip import Drip


def get_number_drip_x(ai_settings, drip_width):
    available_space_x = ai_settings.screen_width - 2 * drip_width
    number_drip_x = int(available_space_x / (2 * drip_width))
    return number_drip_x


def get_number_rows(ai_settings, drip_height):
    number_rows = int(ai_settings.screen_height / (2 * drip_height))
    return number_rows


def create_drip(ai_settings, screen, drips, row_number, drip_number):
    drip = Drip(ai_settings, screen)
    drip_width = drip.rect.width
    drip.rect.x = drip_width + 2 * drip_number * drip_width
    drip.y = drip.rect.height + 2 * row_number * drip.rect.height
    drip.rect.y = drip.y
    drips.add(drip)


def create_fleet(ai_settings, screen, drips):
    drip = Drip(ai_settings, screen)
    number_drip_x = get_number_drip_x(ai_settings, drip.rect.width)
    number_rows = get_number_rows(ai_settings, drip.rect.height)
    for row_number in range(number_rows):
        for drip_number in range(number_drip_x):
            create_drip(ai_settings, screen, drips, row_number, drip_number)


def update_screen(ai_settings, screen, drips):
    screen.fill((0, 0, 0))
    drips.draw(screen)
    pygame.display.flip()


def check_events(ai_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def check_fleet_edges(ai_settings, drips):
    for drip in drips.sprites():
        drip.check_edges()


def update_drips(ai_settings, drips):
    check_fleet_edges(ai_settings, drips)
    drips.update()
