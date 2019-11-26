'''
Author: Andres Mrad (Q-ro)
Date: Tuesday/November/2019 @ 16:56:19
Description: Defines the base class for the game engine scenes  
'''


class SceneBase:
    backgroundColor = 0
    backgroundImage = 0

    def __init__(self, color, image):
        self.backgroundColor = color
        self.backgroundImage = image
