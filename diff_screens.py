import pygame
import sys
from screenmanager import Screen
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

class OrderingScreen(Screen): #first screen where customers order
    def draw(self, screen):
        screen.fill(white)
        font = pygame.font.Font(None, 36)
        text_surf = font.render('Ordering', True, black)
        text_rect = text_surf.get_rect(center = (width//2, height//2))
        screen.blit(text_surf, text_rect)

class CreatingOrderScreen(Screen): #next screen where we create the base of the order
    def draw(self, screen):
        screen.fill(white)
        font = pygame.font.Font(None, 36)
        text_surf = font.render('Creating orders', True, black)
        text_rect = text_surf.get_rect(center = (width//2, height//2))
        screen.blit(text_surf, text_rect)

class BlendingOrderScreen(Screen): #screen where we blend their freezie
    def draw(self, screen):
        screen.fill(white)
        font = pygame.font.Font(None, 36)
        text_surf = font.render('Blending orders', True, black)
        text_rect = text_surf.get_rect(center = (width//2, height//2))
        screen.blit(text_surf, text_rect)

class ToppingOrderScreen(Screen): #screen where we add the toppings
    def draw(self, screen):
        screen.fill(white)
        font = pygame.font.Font(None, 36)
        text_surf = font.render('Topping the orders', True, black)
        text_rect = text_surf.get_rect(center = (width//2, height//2))
        screen.blit(text_surf, text_rect)

class ServingOrderScreen(Screen): #screen where we serve it to the customer
    def draw(self, screen):
        screen.fill(white)
        font = pygame.font.Font(None, 36)
        text_surf = font.render('Creating orders', True, black)
        text_rect = text_surf.get_rect(center = (width//2, height//2))
        screen.blit(text_surf, text_rect)

def main():
    manager = ScreenManager()
    manager.add_screen('Order', OrderingScreen(manager))
    manager.add_screen('Creating order', CreatingOrderScreen(manager))
    manager.add_screen('Blending order', BlendingOrderScreen(manager))
    manager.add_screen('Topping order', ToppingOrderScreen(manager))
    manager.add_screen('Serving order', ServingOrderScreen(manager))

    manager.set_screen('Order') #starting with the order screen

    while True:
        events = pygame.event.get()
        for event in events:
            if event.trype == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        manager.handle_events(events)
        manager.update()
        manager.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()