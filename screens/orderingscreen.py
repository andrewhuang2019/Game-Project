import pygame
from pygame.locals import *
from screens.screen import Screen

#define colors
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

class OrderingScreen(Screen):
    
    def __init__(self):
        super().__init__('Ordering')
        super().update_color(red)

        self.rectangle = pygame.Rect(200, 200, 100, 100)

    def update_display(self):
        self.screen_update() #maintaining the screen
        pygame.draw.rect(self.screen, blue, self.rectangle)
        pygame.display.flip() #refreshes the screen update to get new colors
    

    
