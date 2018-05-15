_author_ = 'Victor Ponciano'

import sys, time
import pygame
import ball, player, wall, constants as c


pygame.init()
#Iniciando Tela
display_game = pygame.display.set_mode((c.display_width, c.display_heigth))
pygame.display.set_caption("Arkanoid")

game_clock = pygame.time.Clock()
pygame.key.set_repeat(c.player_accuracy)

onGame = True
img_bg = pygame.image.load('assets\imagens\Bg.png').convert_alpha()

game_ball = ball.Ball()
game_player = player.Player()
player_points = 0
font = pygame.font.SysFont('Arial', 20)
vidas = 3
wait_init = True

game_wall = wall.Wall(50)


while onGame:

    game_clock.tick(c.game_FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            game_player.playerWorks(event)
            if wait_init == True and event.key == pygame.K_SPACE:
                wait_init = False
                if game_ball.rect.centerx < c.display_heigth / 2:
                    game_ball.speed = [-3, 3]
                else:
                    game_ball.speed = [-3, -3]


    display_game.blit(img_bg, (0, 0))

    if wait_init == False:
        game_ball.ballWorks()
    else:
        game_ball.rect.midbottom = game_player.rect.midtop

    if pygame.sprite.collide_rect(game_ball, game_player):
        game_ball.speed[1] = -c.ball_speedY

    blockList = pygame.sprite.spritecollide(game_ball, game_wall, False)
    if blockList:
        block = blockList[0]
        cx = game_ball.rect.centerx
        if cx < block.rect.left or cx > block.rect.right:
            game_ball.speed[0] = -game_ball.speed[0]
        else:
            game_ball.speed[1] = -game_ball.speed[1]
        player_points = player_points + 10
        game_wall.remove(block)

    if game_ball.rect.bottom > c.display_heigth:
        vidas -= 1
        wait_init = True


    display_game.blit(game_ball.image,game_ball.rect)
    display_game.blit(game_player.image,game_player.rect)
    game_wall.draw(display_game)
    text = font.render(str(player_points).zfill(5), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topleft = [0, 0]
    lifeEnca = "vidas: "+ str(vidas).zfill(2)
    life_txt = font.render(lifeEnca, True, (255,255,255))
    life_text_rect = life_txt.get_rect()
    life_text_rect.topright = [c.display_width, 0]
    display_game.blit(text, text_rect)
    display_game.blit(life_txt, life_text_rect)

    pygame.display.update()

    if vidas <=0:
        game_over()

    def game_over():
        font = pygame.font.SysFont('Arial', 72)
        text = font.render("Game Over :(", True,(255,255,255))
        text_rect = text.get_rect()
        text_rect.center = [c.display_width/2, c.display_heigth/2]

        display_game.blit(text, text_rect)
        pygame.display.update()
        time.sleep(3)
        sys.exit()

