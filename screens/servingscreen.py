import pygame
import sys
from screens.screen import Screen
from screens.screenmanager import ScreenManager

#define colors
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

class ServingScreen(Screen): #screen where we serve it to the customer
    def __init__(self):
        super().__init__('Serving')
        #super().update_color(black)
    