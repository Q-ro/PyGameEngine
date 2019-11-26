'''
Author: Andres Mrad (Q-ro)
Date: Tuesday/November/2019 @ 16:58:05
Description:  A ball game object 
'''

from pygame.locals import *


class Ball:
    pos = 0  # The ball's current position
    ball = 0  # The ball's image
    ballrect = 0  # The ball bounding box
    speed = [0.9, 1.3]  # Ball's moving speed
    xBound = 0
    yBound = 0

    def __init__(self, sprite, speed, xBound, yBound):
        self.ball = sprite
        self.ballrect = self.ball.get_rect()
        self.speed = speed
        self.xBound = xBound
        self.yBound = yBound

    def moveBall(self):
        self.ballrect = self.ballrect.move(self.speed)
        self.bounceBall()

    def bounceBall(self):
        if self.ballrect.left < 0 or self.ballrect.right > self.xBound:
            self.speed[0] = -self.speed[0]
        if self.ballrect.top < 0 or self.ballrect.bottom > self.yBound:
            self.speed[1] = -self.speed[1]
