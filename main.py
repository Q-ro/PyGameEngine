'''
Author: Andres Mrad (Q-ro)
Date: Tuesday 19/November/2019 @ 16:58:50
Description: A simple OOP game engine for python using pygames 
'''

import pygame
from events.customEvents import CUSTOM_EVENTS_DIC
from Scenes.ballScene import BallScene
from Scenes.menuScene import MenuScene


class App:
    _scenes = []  # A list containing all the game scenes
    _currentScene = 0  # the scene being currently displayed
    _currentSceneIndex = 0  # The scene being currently displayed
    _display_surf = None # The pygame display surface to be used by the program for rendering

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 800, 640
        pygame.display.set_caption('Test python game')

    def init_scenes(self, parameter_list):
        self._currentSceneIndex = 0
        self._scenes.append(MenuScene(pygame, self.width, self.height))
        self._scenes.append(BallScene(pygame, self.width, self.height))
        self._currentScene = self._scenes[self._currentSceneIndex]

        pass

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.init_scenes(self)

    def on_event(self, event):
        keys = pygame.key.get_pressed()

        if (event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
            self._running = False

        if event.type ==  CUSTOM_EVENTS_DIC['CHANGE_SCENE_EVENT']:
            self.on_change_scene(event.sceneIndex)

        self._currentScene.on_event(event, pygame)

    def on_change_scene(self, sceneIndex):
        print("CAMBIO")
        print(sceneIndex)
        print(self._currentSceneIndex)
        self._currentSceneIndex = sceneIndex
        self._currentScene = self._scenes[self._currentSceneIndex]

    def on_loop(self):
        self._currentScene.on_loop()

    def on_render(self):
        self._currentScene.on_render(self._display_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()