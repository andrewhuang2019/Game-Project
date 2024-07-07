import pygame

class Screen:
    def __init__(self, title, width=1000, height=700, fill=(0,0,0)):
        self.title = title

        self.fill = fill

        self.width = width
        
        self.height = height

        self.is_current = False

    def make_current_screen(self):
        pygame.display.set_caption(self.title)
        self.is_current = True
        self.screen = pygame.display.set_mode((self.width, self.height))

    def end_current_screen(self):
        self.is_current = False

    def get_current(self):
        return self.is_current 
    
    def screen_update(self):
        if self.is_current:
            self.screen.fill(self.fill)

'''
if __name__ == '__main__':
    pygame.init()
    screen1 = Screen('Test')
    while True:
        screen1.make_current_screen()'''