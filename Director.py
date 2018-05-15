_author_ = 'Victor Ponciano'

import pygame, constants as c, time, scenes

class Director:
    def __init__(self, title = '', res = (width, heigth)):
        pygame.init()
        self.display_game = pygame.display.set_mode((res))
        pygame.display.set_caption(title)
        self.game_clock = pygame.time.Clock()
        self.scene = None
        self.scenes = {}

    def execute(self, scene_init, fps):
        self.scene = self.scenes[scene_init]
        onGame = True
        while onGame:
            self.game_clock.tick(c.game_FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  onGame = False
            self.scene.read_events(event)
            self.scene.update()
            self.scene.distro(self.display_game)

            self.selectScene(self.scene.nextScene)

            if onGame:
                onGame = self.scene.onGame

            pygame.display.flip()

        time.sleep(3)

    def selectScene(self, nextScene):
        if nextScene:
            if nextScene not in self.scenes:
                self.addScene(nextScene)
            self.scene = self.scenes[nextScene]

    def addScene(self, scene):
        sceneClass = 'Scene' + scene
        sceneObj = globals()[sceneClass]
        self.scenes[scene] = sceneObj()
