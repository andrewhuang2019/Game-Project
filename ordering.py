import pygame
from pygame.locals import *
from screen import Screen

class OrderingScreen:
    
    def __init__(self):
        self.screen = Screen('Ordering') #changing fill color from black
        self.screen.update_color((218,194,238))

    def make_current_screen(self):
        self.screen.make_current_screen() #calling the method from screen.py
    
    def display_current(self):
        self.screen.screen_update() #maintaining the screen
        pygame.display.flip() #refreshes the screen update to get new colors
    

    
