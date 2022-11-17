import pygame
import sys
from pygame.sprite import Sprite


class Final_Game:

    def __init__(self,screen):

        pygame.init()
        self.screen = screen
        self.image1 = pygame.image.load('tank_blue.png')
        self.image2 = pygame.image.load('tank_red.png')
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect1.left = self.screen.get_rect().left
        self.rect2.right = self.screen.get_rect().right
        self.y1 = float(self.rect1.y)
        self.x1 = float(self.rect1.x)
        self.x2 = float(self.rect2.x)
        self.y2 = float(self.rect2.y)
        self.moving_up1 = False
        self.moving_up2 = False
        self.moving_down1 = False
        self.moving_down2 = False
        self.moving_right1 = False
        self.moving_right2 = False
        self.moving_left1 = False
        self.moving_left2 = False

    def _check_events(self,event):
        for events in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.moving_right1 = True
        elif event.key == pygame.K_LEFT:
            self.moving_left1 = True
        if event.key == pygame.K_UP:
            self.moving_up1 = True
        elif event.key == pygame.K_DOWN:
            self.moving_down1 = True
        #elif event.key == pygame.K_SPACE:
            #self._fire_bullet()
        if event.key == pygame.K_w:
            self.moving_up2 = True
        elif event.key == pygame.K_s:
            self.moving_down2 = True
        if event.key == pygame.K_a:
            self.moving_left2 = True
        elif event.key == pygame.K_d:
            self.moving_right2 = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.moving_left = False
        if event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False
        if event.key == pygame.K_w:
            self.moving_up2 = False
        elif event.key == pygame.K_s:
            self.moving_down2 = False
        if event.key == pygame.K_a:
            self.moving_left2 = False
        elif event.key == pygame.K_d:
            self.moving_right2 = False

    def update(self): #CHANGE VARIABLES
        if self.moving_right1 and self.rect.right < self.screen_rect.right:
            self.x1 += 1
        if self.moving_left and self.rect.left > 0:
            self.x1 -= 1
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y1 -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y1 += 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= rocket_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += rocket_speed
        # update rect object from self.x
        # self.rect.x = self.x
        self.rect.y = self.y

        self.rect1.x = self.x1
        self.rect1.y = self.y2