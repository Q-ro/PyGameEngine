"""
Author: Andres Mrad (Q-ro)
Date: Thursday 06/February/2020 @ 10:59:15
Description:  Main Menu for the test game 
"""

from Scenes.sceneBase import SceneBase
from events.customEvents import CUSTOM_EVENTS_DIC


class MenuScene(SceneBase):

    textToDisplay = "Main Menu"
    menuItems = ["New Game, Load Game, Options, Exit"]
    currentMenuItem = 0
    green = (0, 255, 0)
    blue = (0, 0, 128)
    text = 0
    textRect = 0

    def __init__(self, pygame, width, height):
        backgroundColor = 0, 1, 1
        SceneBase.__init__(self, backgroundColor, 0, width, height)
        font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = font.render('Press start you fuck ! ', True, self.green,
                                self.blue)
        self.textRect = self.text.get_rect()

        # set the center of the rectangular object.
        self.textRect.center = (self._width // 2, self._height // 2)
        pass

    def on_lopp(self):

        pass

    def on_event(self, event, pygame):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            # print(event)
            # CHANGE_SCENE_EVENT = pygame.USEREVENT+1 # A custome event that let's the program know what scene to switch to
            changeScene = pygame.event.Event(
                CUSTOM_EVENTS_DIC['CHANGE_SCENE_EVENT'], sceneIndex=1)
            # changeScene = pygame.event.Event(CHANGE_SCENE_EVENT, sceneIndex = 1)
            pygame.event.post(changeScene)
        pass

    def on_render(self, display_surf):
        SceneBase.on_render(self, display_surf)
        # display_surf.blit(self.ball.ball, self.ball.ballrect)
        display_surf.blit(self.text, self.textRect)
        pass