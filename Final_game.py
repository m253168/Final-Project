import pygame
import sys
from pygame.sprite import Sprite
from bullet1 import Bullet1
from bullet2 import Bullet2


class Final_Game:

    def __init__(self,screen):

        pygame.init()
        self.screen = screen
        self.image1 = pygame.image.load('tank_blue.png')
        self.image2 = pygame.image.load('tank_red.png')
        self.heart = pygame.image.load('heart.bmp')
        self.grey_heart = pygame.image.load('greyheart.bmp.png')
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect1.midleft = self.screen.get_rect().midleft
        self.rect2.midright = self.screen.get_rect().midright
        self.screen_rect = screen.get_rect()
        self.screen_width = float(self.screen_rect.x)
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
        self.bullet1 = pygame.sprite.Group()
        self.bullet2 = pygame.sprite.Group()
        self.bullet_allowed = 5
        self.boom = pygame.mixer.Sound('boom.wav')
        self.font = pygame.font.Font('freesansbold.ttf',36)
        self.text = pygame.font.Font.render(self,"Health",False,(255,255,255))
        #self.text_rect = self.text.get_rect()
        #self.text_rect.center = self.screen.get_rect().center


    def _check_events(self):
        """check and respond to keypresses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """Check for when buttons are pressed down"""
        if event.key == pygame.K_RIGHT:
            self.moving_right2 = True
        elif event.key == pygame.K_LEFT:
            self.moving_left2 = True
        if event.key == pygame.K_UP:
            self.moving_up2 = True
        elif event.key == pygame.K_DOWN:
            self.moving_down2 = True
        elif event.key == pygame.K_m:
            self._fire_bullet2()
        elif event.key == pygame.K_b:
            self._fire_bullet1()
        if event.key == pygame.K_w:
            self.moving_up1 = True
        elif event.key == pygame.K_s:
            self.moving_down1 = True
        if event.key == pygame.K_a:
            self.moving_left1 = True
        elif event.key == pygame.K_d:
            self.moving_right1 = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Check for when the buttons are released"""
        if event.key == pygame.K_RIGHT:
            self.moving_right2 = False
        elif event.key == pygame.K_LEFT:
            self.moving_left2 = False
        if event.key == pygame.K_UP:
            self.moving_up2 = False
        elif event.key == pygame.K_DOWN:
            self.moving_down2 = False
        if event.key == pygame.K_w:
            self.moving_up1 = False
        elif event.key == pygame.K_s:
            self.moving_down1 = False
        if event.key == pygame.K_a:
            self.moving_left1 = False
        elif event.key == pygame.K_d:
            self.moving_right1 = False

    def _fire_bullet1(self):
        """Checks for amount of bullets and calls on the bullet class to fire a bullet and play a sound"""
        if len(self.bullet1) < self.bullet_allowed:
            new_bullet1 = Bullet1(self)
            self.bullet1.add(new_bullet1)
            pygame.mixer.Sound.play(self.boom)

    def _fire_bullet2(self):
        if len(self.bullet2) < self.bullet_allowed:
            new_bullet2 = Bullet2(self)
            self.bullet2.add(new_bullet2)
            pygame.mixer.Sound.play(self.boom)

    def update(self):
        """Updates screen based on the key presses before based on the predetermined tank speed"""
        if self.moving_right1 and self.rect1.right < self.screen_rect.right:
            self.x1 += tank_speed
        if self.moving_left1 and self.rect1.left > 0:
            self.x1 -= tank_speed
        if self.moving_up1 and self.rect1.top > self.screen_rect.top:
            self.y1 -= tank_speed
        if self.moving_down1 and self.rect1.bottom < self.screen_rect.bottom:
            self.y1 += tank_speed
        if self.moving_right2 and self.rect2.right < self.screen_rect.right:
            self.x2 += tank_speed
        if self.moving_left2 and self.rect2.left > 0:
            self.x2 -= tank_speed
        if self.moving_up2 and self.rect2.top > self.screen_rect.top:
            self.y2 -= tank_speed
        if self.moving_down2 and self.rect2.bottom < self.screen_rect.bottom:
            self.y2 += tank_speed

        self.rect2.x = self.x2
        self.rect2.y = self.y2

        self.rect1.x = self.x1
        self.rect1.y = self.y1

    def draw(self):
        """Draw on the screen"""
        self.screen.fill((40,30,20))
        self.screen.blit(self.image1, self.rect1)
        self.screen.blit(self.image2, self.rect2)
        for bullet in self.bullet1.sprites():
            bullet.draw_bullet()
        for bullet in self.bullet2.sprites():
            bullet.draw_bullet()
        self.screen.blit(self.heart, (0,0))
        self.screen.blit(self.heart,(50,0))
        self.screen.blit(self.heart,(100,0))
        self.screen.blit(self.heart,(150,0))
        self.screen.blit(self.grey_heart,(200,0))
        print(self.screen_width-50)
        self.screen.blit(self.heart,(self.screen_rect.rightq-50,0))
        #self.screen.blit(self.text,self.text_rect)
        pygame.display.flip()



    def run_game(self):
        """calls on all of the methods and runs them"""
        while True:
            self._check_events()
            self.update()
            self.draw()
            self.bullet1.update()
            self.bullet2.update()

            for bullet in self.bullet1.copy():
                if bullet.rect1.right >= self.screen_rect.right:
                    self.bullet1.remove(bullet)
            for bullet in self.bullet2.copy():
                if bullet.rect2.left <= self.screen_rect.left:
                    self.bullet2.remove(bullet)

tank_speed = .75
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
final_game = Final_Game(screen)
final_game.run_game()


