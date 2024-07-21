import pygame
import sys
from screens.screen import Screen
from screens.screenmanager import ScreenManager

#define colors
white = (255, 255, 255)
bliue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

class BlendingScreen(Screen): #screen where we blend their freezie
    def __init__(self):
        super().__init__('Blending')
        super().update_color(white)