_author_ = 'Victor Ponciano'

import sys, time
import pygame
import ball, player, wall, constants as c, scenes, Director


class Level1(scenes.Scene):
    def __init__(self):
        scenes.Scene.__init__(self)
        self.game_ball = ball.Ball()
        self.game_player = player.Player()
        self.game_wall = wall.Wall(50)
        self.player_points = 0
        self.vidas = 3
        self.wait_init = True
        pygame.key.set_repeat(c.player_accuracy)
        self.img_bg = pygame.image.load('assets\imagens\Bg.png').convert_alpha()
        self.font = pygame.font.SysFont('Arial', 20)

    def read_events(self, events):
        for event in events:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.game_player.playerWorks(event)
                    if wait_init == True and event.key == pygame.K_SPACE:
                        wait_init = False
                        if self.game_ball.rect.centerx < c.display_heigth / 2:
                            self.game_ball.speed = [-3, 3]
                        else:
                            self.game_ball.speed = [-3, -3]

    def update(self):
        if self.wait_init == False:
            self.game_ball.ballWorks()
        else:
            self.game_ball.rect.midbottom = self.game_player.rect.midtop

        if pygame.sprite.collide_rect(self.game_ball, self.game_player):
            self.game_ball.speed[1] = -c.ball_speedY

        blockList = pygame.sprite.spritecollide(self.game_ball, self.game_wall, False)
        if blockList:
            block = blockList[0]
            cx = self.game_ball.rect.centerx
            if cx < block.rect.left or cx > block.rect.right:
                self.game_ball.speed[0] = -self.game_ball.speed[0]
            else:
                self.game_ball.speed[1] = -self.game_ball.speed[1]
            player_points = self.player_points + 10
            self.game_wall.remove(block)

        if self.game_ball.rect.bottom > c.display_heigth:
            self.vidas -= 1
            wait_init = True

        if self.vidas <= 0:
            self.game_over()
            self.change_scene('GameOver')

    def Draw(self, screen):

        self.display_game.blit(self.img_bg, (0, 0))
        self.display_game.blit(self.game_ball.image, self.game_ball.rect)
        self.display_game.blit(self.game_player.image, self.game_player.rect)
        self.game_wall.draw(self.display_game)
        text = self.font.render(str(self.player_points).zfill(5), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topleft = [0, 0]
        lifeEnca = "vidas: " + str(self.vidas).zfill(2)
        life_txt = self.font.render(lifeEnca, True, (255, 255, 255))
        life_text_rect = life_txt.get_rect()
        life_text_rect.topright = [c.display_width, 0]
        self.display_game.blit(text, text_rect)
        self.display_game.blit(life_txt, life_text_rect)


director = Director('Arkanoid', (c.display_width, c.display_heigth))
director.addScene('Level1')
director.execute('Level1')
