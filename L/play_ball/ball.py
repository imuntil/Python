import pygame
from random import randint


class Ball():
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.rect = pygame.Rect(0, 0, ai_settings.ball_speed_factor * 2,
                                ai_settings.ball_radius * 2)
        self.color = (0, 0, 0)
        self.speed_factor = ai_settings.ball_speed_factor
        self.reset_ball()

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, [self.x, self.y],
                           self.ai_settings.ball_radius)

    def reset_ball(self):
        self.x = randint(0, self.screen_rect.width)
        self.y = -self.ai_settings.ball_radius * 2
        self.set_ball_rect()

    def update(self):
        self.y += self.ai_settings.ball_speed_factor
        self.set_ball_rect()

    def set_ball_rect(self):
        self.rect.x = self.x - self.ai_settings.ball_radius
        self.rect.y = self.y - self.ai_settings.ball_radius
