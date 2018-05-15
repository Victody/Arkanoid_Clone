_author_ = 'Victor Ponciano'

import pygame, constants as c

class Scene:
    def __init__(self):
        self.nextScene = False
        self.onGame = True

    def read_events(self, events):
        pass

    def update(self):
        pass

    def distro(self, secreen):
        pass

    def change_scene(self, scene):
        self.nextScene = scene
