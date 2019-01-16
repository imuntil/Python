import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    stats = GameStats(ai_settings)

    ship = Ship(ai_settings, screen)

    play_button = Button(ai_settings, screen, 'PLAY')

    scoreboard = Scoreboard(ai_settings, screen, stats)

    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, aliens, bullets, stats,
                        play_button, scoreboard)
        if (stats.game_active):
            ship.update()
            gf.update_bullets(ai_settings, bullets, aliens, screen, ship,
                              stats, scoreboard)
            gf.update_aliens(ai_settings, screen, ship, stats, bullets, aliens,
                             scoreboard)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stats,
                         play_button, scoreboard)


run_game()
