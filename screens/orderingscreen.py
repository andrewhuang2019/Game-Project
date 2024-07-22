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

        self.rectangle = pygame.Rect(200, 200, 100, 100)
        self.ingredient_button = Button(200, 100, 75, 75, "I", blue, green)

    def update_display(self):
        
        self.screen.fill(self.fill)
        pygame.draw.rect(self.screen, blue, self.rectangle)
        self.ingredient_button.draw(self.screen)
        pygame.display.flip() #refreshes the screen update to get new colors

    def ingredient_button_is_clicked(self, event):
        return self.ingredient_button.is_clicked(event)
    

    
