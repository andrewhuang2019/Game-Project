import pygame
from pygame.locals import *
from screens.screen import Screen
from button import Button

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

    def update_display(self):
        
        self.screen.fill(self.fill)
        #pygame.draw.rect(self.screen, blue, self.rectangle)
        self.building_button.draw(self.screen)#refreshes the screen update to get new colors
        self.blending_button.draw(self.screen)
        self.topping_botton.draw(self.screen)
        self.serving_button.draw(self.screen)
        pygame.display.flip()


    
