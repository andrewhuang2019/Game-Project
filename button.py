import pygame
import sys
from pygame.locals import *
import math

#define colors
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

#set up display
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Button Example')


class Button: #rectangular button
    def __init__(self, x, y, width, height, text, color, hover_color, shape='rect'):
        self.rect = pygame.Rect(x, y, width, height) #creates new rectangle we're storing w/attributes
        #self.circ = (x, y) if shape == 'circle' else None
        self.text = text
        self.color = color
        #self.shape = shape
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, 36) #None is default font and 36 is how big
        self.text_surf = self.font.render(text, True, white)
        self.text_rect = self.text_surf.get_rect(center = self.rect.center)
    
    def draw(self, screen):
        mousepos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousepos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        text_surf = self.font.render(self.text, True, white)
        text_rect = text_surf.get_rect(center = self.rect.center)
        screen.blit(text_surf, text_rect)
    
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
            #elif self.circ.collidepoint(event.pos):
                distance = math.sqrt((event.pos[0] - self.circ[0])**2 + (event.pos[1] - self.circ[1])**2)
                if distance <= self.radius:
                    return True
        return False

def main():
    button = Button(350, 250, 100, 50, 'Click Me', (255, 0, 0), (200, 0, 0))
    
    while True:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if button.is_clicked(event):
                print('Button clicked :)')
        
        button.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()