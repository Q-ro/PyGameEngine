"""
Author: Andres Mrad (Q-ro)
Date: Thursday 13/February/2020 @ 10:40:36
Description:  A dictionary that defines all the custom events for the game engine 
"""
import pygame

CUSTOM_EVENTS_DIC = {
    'CHANGE_SCENE_EVENT': pygame.USEREVENT + 1,  # A custome event that let's the program know what scene to switch to 
    'PAUSE_SCENE_EVENT': pygame.USEREVENT + 2,  # A custome event that let's the program know it's time to halt excecution
    'RESTART_SCENE_EVENT': pygame.USEREVENT + 3,  # A custome event that let's the program know we have to reload the scene (set it back to it's default state) 
    'EXIT_GAME_EVENT': pygame.QUIT,  # A custome event that let's the program know it's time to shut itself down
}
