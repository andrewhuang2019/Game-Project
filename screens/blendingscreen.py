import pygame
import sys
from screens.screen import Screen
from screens.screenmanager import ScreenManager
from button import Button

#define colors
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

class BlendingScreen(Screen): #screen where we blend their freezie
    def __init__(self):
        super().__init__('Blending')
        super().update_color(white)

        self.rectangle = pygame.Rect(200, 200, 100, 100)
        self.building_button = Button(200, 160, 75, 75, "Building", blue, green)
        self.blending_button = Button(200, 230, 75, 75, "Blending", blue, green)
        self.topping_botton = Button(200, 160, 75, 75, "Topping", blue, green)
        self.serving_button = Button(200, 160, 75, 75, "Serving", blue, green)

    def update_display(self):
        
        self.screen.fill(self.fill)
        pygame.draw.rect(self.screen, blue, self.rectangle)
        self.building_button.draw(self.screen)
        pygame.display.flip() #refreshes the screen update to get new colors
        self.blending_button.draw(self.screen)
        pygame.display.flip()
        self.topping_botton.draw(self.screen)
        pygame.display.flip()
        self.serving_button.draw(self.screen)
        pygame.display.flip()

    def building_button_is_clicked(self, event):
        return self.building_button.is_clicked(event)
    
    def blending_button_is_clicked(self, event):
        return self.blending_button.is_clicked(event)
    
    def topping_button_is_clicked(self, event):
        return self.topping_botton.is_clicked(event)
    
    def serving_button_is_clicked(self, event):
        return self.serving_button.is_clicked(event)