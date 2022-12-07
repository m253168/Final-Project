import pygame
from pygame.sprite import Sprite


pygame.init()


class Bullet1(Sprite):

    def __init__(self,final_game):
        super().__init__()
        self.bullet_speed = 2
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (0,0,255)
        self.screen = final_game.screen
        self.bullet_rect1 = pygame.Rect(0,0,self.bullet_width,self.bullet_height)
        self.bullet_rect1.midright = final_game.rect1.midright
        self.x1 = float(self.bullet_rect1.x)

    def update(self):
        self.x1 += self.bullet_speed
        self.bullet_rect1.x = self.x1

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.bullet_color,self.bullet_rect1)
