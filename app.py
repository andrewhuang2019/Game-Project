import pygame
from pygame.locals import *

from screens.screen import Screen
from screens.blendingscreen import BlendingScreen
from screens.ingredientscreen import IngredientScreen
from screens.orderingscreen import OrderingScreen
from screens.toppingscreen import ToppingScreen
from screens.servingscreen import ServingScreen
from screens.screenmanager import ScreenManager


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None

        self.ordering_screen = OrderingScreen()
        self.ingredient_screen = IngredientScreen()
        self.blending_screen = BlendingScreen()
        self.topping_screen = ToppingScreen()
        self.serving_screen = ServingScreen()
        
        #self.screen_manager = ScreenManager()

        

    def on_init(self):
        pygame.init() #starts pygame module
        self._display_surf = pygame.display.set_mode((1000,700), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.ordering_screen.make_current_screen()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            
    def on_loop(self):
        pass

    def on_render(self):
        self.ordering_screen.update_display()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()