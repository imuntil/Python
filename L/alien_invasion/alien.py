import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ 外星人class """

    def __init__(self, ai_settings, screen):
        """ 初始化alien并设置起始位置 """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """ 在制定的位置绘制alien """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ 向右/向左移动alien """
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ 检测alien是否撞到屏幕边缘，是就返回True """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
