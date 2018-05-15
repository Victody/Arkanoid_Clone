_author_ = 'Victor Ponciano'

import pygame, block, constants as c

class Wall(pygame.sprite.Group):
    def __init__(self, numBlocks):
        pygame.sprite.Group.__init__(self)

        wall_block_posX = 0
        wall_block_posY = 20

        for i in range(numBlocks):
            blocks = block.Block((wall_block_posX, wall_block_posY))
            self.add((blocks))
            wall_block_posX += blocks.rect.width

            if wall_block_posX >= c.display_width:
                wall_block_posX = 0
                wall_block_posY += blocks.rect.height

