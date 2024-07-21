import pygame
import sys
from screen import Screen
from screenmanager import ScreenManager

#define colors
white = (255, 255, 255)
bliue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

#set up display
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))

class BlendingOrderScreen(Screen): #screen where we blend their freezie
    def draw(self, screen):
        screen.fill(white)
        font = pygame.font.Font(None, 36)
        text_surf = font.render('Blending orders', True, black)
        text_rect = text_surf.get_rect(center = (width//2, height//2))
        screen.blit(text_surf, text_rect)

def main():
    manager = ScreenManager()
    manager.add_screen('Blending order', BlendingOrderScreen(manager))

    #manager.set_screen('Order') #starting with the order screen

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        manager.handle_events(events)
        manager.update()
        manager.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()