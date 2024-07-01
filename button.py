import pygame
from pygame.locals import *

class Button: #rectangular button
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height) #creates new rectangle we're storing w/attributes
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, 36) #None is default font and 36 is how big
        