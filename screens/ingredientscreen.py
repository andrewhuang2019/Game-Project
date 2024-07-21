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

class IngredientScreen(Screen): #next screen where we create the base of the order
    def __init__(self):
        super().__init__('Ingredient')
        super().update_color(green)
    