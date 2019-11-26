'''
Author: Andres Mrad (Q-ro)
Date: Tuesday/November/2019 @ 16:58:50
Description:  A simple OOP game engine for python using pygames 
'''

from ball import Ball  #Add the ball class
import pygame


class App:
    scenes = []  # A list containing all the game scenes
    ball = 0  # A reference to a ball object to be bounced across the screen

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 800, 640
        self.ball = Ball(pygame.image.load("intro_ball.gif"), [1.9, 1.1],
                         self.width, self.height)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.ball.moveBall()

    def on_render(self):
        black = 0, 0, 0
        self._display_surf.fill(black)
        self._display_surf.blit(self.ball.ball, self.ball.ballrect)
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