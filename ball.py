_author_ = 'Victor Ponciano'

import pygame, constants as c

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/imagens/Arkanoid_Ball.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = c.display_width / 2
        self.rect.centery = c.display_heigth /2
        self.speed = [c.ball_speedX, c.ball_speedY]

    def ballWorks(self):

        if self.rect.top <=0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= c.display_width or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]

        self.rect.move_ip(self.speed)
