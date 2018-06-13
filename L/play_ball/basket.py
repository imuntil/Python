import pygame


class Basket():
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.rect = pygame.Rect(
            0, 0, ai_settings.basket_width, ai_settings.basket_height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.x = float(self.rect.x)
        self.color = ai_settings.basket_color
        self.speed_factor = ai_settings.basket_speed_factor

        self.moving = []

    def update(self):
        if len(self.moving) == 0:
            return
        elif 'R' in self.moving and 'L' in self.moving:
            return
        elif 'R' in self.moving and self.rect.right <= self.screen_rect.right:
            self.x += self.ai_settings.basket_speed_factor
        elif 'L' in self.moving and self.rect.left >= 0:
            self.x -= self.ai_settings.basket_speed_factor

        self.rect.x = self.x

    def draw_basket(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
