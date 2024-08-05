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

class ToppingScreen(Screen): #screen where we add the toppings
    def __init__(self):
        super().__init__('Topping')
        #super().update_color(blue)