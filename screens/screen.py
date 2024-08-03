import pygame
from button import Button


white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

class Screen:
    def __init__(self, title, width=1000, height=700, fill=(0,0,0)):
        self.title = title

        self.fill = fill

        self.width = width
        
        self.height = height

        self.is_current = False

        self.ordering_button = Button(100, 160, 75, 75, "Ordering", blue, green)
        self.building_button = Button(200, 160, 75, 75, "Building", blue, green)
        self.blending_button = Button(300, 160, 75, 75, "Blending", blue, green)
        self.topping_button = Button(400, 160, 75, 75, "Topping", blue, green)

    def make_current_screen(self):
        pygame.display.set_caption(self.title)
        self.is_current = True
        self.screen = pygame.display.set_mode((self.width, self.height))

    def end_current_screen(self):
        self.is_current = False

    def get_current(self):
        return self.is_current 
    
    def update_display(self):
        if self.is_current:
            self.screen.fill(self.fill) #maintaining the screen
            self.building_button.draw(self.screen) #refreshes the screen update to get new colors
            self.blending_button.draw(self.screen)
            self.topping_button.draw(self.screen)
            self.ordering_button.draw(self.screen)
            pygame.display.flip() #refreshes the screen update to get new colors
        
    def update_color(self, fill):
        self.fill = fill

    def building_button_is_clicked(self, event):
        return self.building_button.is_clicked(event)
    
    def blending_button_is_clicked(self, event):
        return self.blending_button.is_clicked(event)
    
    def topping_button_is_clicked(self, event):
        return self.topping_button.is_clicked(event)
    
    def ordering_button_is_clicked(self, event):
        return self.ordering_button.is_clicked(event)

'''
if __name__ == '__main__':
    pygame.init()
    screen1 = Screen('Test')
    while True:
        screen1.make_current_screen()'''