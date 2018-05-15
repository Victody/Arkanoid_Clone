_author_ = 'Victor Ponciano'

import sys, time
import pygame
import ball, player, wall, constants as c, scenes

class sceneGameOver:
    def update(self):
        self.onGame = False

    def draw(self, screen):
        font = pygame.font.SysFont('Arial', 72)
        text = font.render("Game Over :(", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = [c.display_width / 2, c.display_heigth / 2]

        self.display_game.blit(text, text_rect)
