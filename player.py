_author_ = 'Victor Ponciano'

import pygame, constants as c

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/imagens/Arkanoid_Player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (c.display_width/2, c.display_heigth-16)
        self.speed = [c.player_init_speed, c.player_init_speed]

    def playerWorks(self, event):
        if event.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-c.player_speed,c.player_init_speed]
        elif event.key == pygame.K_RIGHT and self.rect.right < c.display_width:
            self.speed = [c.player_speed,c.player_init_speed]
        else:
            self.speed = [c.player_init_speed, c.player_init_speed]

        self.rect.move_ip(self.speed)
