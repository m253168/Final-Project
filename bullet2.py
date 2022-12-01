import pygame
from pygame.sprite import Sprite

pygame.init()


class Bullet2(Sprite):

    def __init__(self, final_game):
        super().__init__()
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.screen = final_game.screen
        self.rect2 = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect2.midleft = final_game.rect2.midleft
        self.x2 = float(self.rect2.x)

    def update(self):
        self.x2 -= self.bullet_speed
        self.rect2.x = self.x2

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect2)
