import pygame


class Rocket():
    def __init__(self, ai_settings, screen):
        """初始化火箭设置"""
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将火箭放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.center = (float(self.rect.centerx), float(self.rect.centery))

        # 移动标志
        self.move = []

    def update(self):
        """根据移动标志调整飞船的位置"""
        if 'RIGHT' in self.move  and self.rect.right < self.screen_rect.right:
            self.center = (self.center[0] + self.ai_settings.rocket_speed,
                           self.center[1])
        if 'LEFT' in self.move and self.rect.left > 0:
            self.center = (self.center[0] - self.ai_settings.rocket_speed,
                           self.center[1])
        if 'DOWN' in self.move and self.rect.bottom < self.screen_rect.bottom:
            self.center = (self.center[0],
                           self.center[1] + self.ai_settings.rocket_speed)
        if 'UP' in self.move and self.rect.top > 0:
            self.center = (self.center[0],
                           self.center[1] - self.ai_settings.rocket_speed)

        self.rect.centerx = self.center[0]
        self.rect.centery = self.center[1]

    def blitme(self):
        """绘制火箭"""
        self.screen.blit(self.image, self.rect)