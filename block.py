_author_ = 'Victor Ponciano'

import pygame, constants as c

class Block(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/imagens/enemy.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position


