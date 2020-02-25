'''
Author: Andres Mrad (Q-ro)
Date: Tuesday/November/2019 @ 16:56:19
Description: Defines the base class for the game engine scenes  
'''


class SceneBase:
    _backgroundColor = None
    _backgroundImage = None
    _width = 0
    _height = 0

    def __init__(self, color, image, width, height):
        self._backgroundColor = color
        self._backgroundImage = image
        self._width = width
        self._height = height

    def on_event(self,event,pygame):
        pass

    def on_loop(self):
        pass

    def on_render(self, display_surf):
        display_surf.fill(self._backgroundColor)
        pass
