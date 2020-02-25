"""
Author: Andres Mrad (Q-ro)
Date: Tuesday 04/February/2020 @ 16:37:20
Description:  A scene containing a ball bouncing aroun the screen 
"""

from Scenes.sceneBase import SceneBase
from GameObjects.ball import Ball  #Add the ball class


class BallScene(SceneBase):

    ball = 0  # A reference to a ball object to be bounced across the screen

    def __init__(self, pygame, width, height):
        backgroundColor = 0, 0, 0
        # self._display_surf.fill(black)
        SceneBase.__init__(self, backgroundColor, 0, width, height)
        self.ball = Ball(pygame.image.load("intro_ball.gif"), [1.9, 1.1],
                         self._width, self._height)

    def on_event(self,event,pygame):
            pass

    def on_loop(self):
        self.ball.moveBall()
        pass

    def on_render(self, display_surf):
        SceneBase.on_render(self,display_surf)
        display_surf.blit(self.ball.ball, self.ball.ballrect)
        pass