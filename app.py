import pygame
from pygame.locals import *

from screens.screen import Screen
from screens.blendingscreen import BlendingScreen
from screens.buildingscreen import BuildingScreen
from screens.orderingscreen import OrderingScreen
from screens.toppingscreen import ToppingScreen
from screens.servingscreen import ServingScreen
from screens.screenmanager import ScreenManager


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None

    def on_init(self):
        pygame.init() #starts pygame module

        self.ordering_screen = OrderingScreen()
        self.building_screen = BuildingScreen()
        self.blending_screen = BlendingScreen()
        self.topping_screen = ToppingScreen()
        self.serving_screen = ServingScreen()

        self.screen_manager = ScreenManager()

        self._display_surf = pygame.display.set_mode((1000,700), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.ordering_screen.make_current_screen()
        self.screen_manager.cur_screen = self.ordering_screen

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        self.screen_manager.is_blending_button_clicked(self.blending_screen, event)
        self.screen_manager.is_topping_button_clicked(self.topping_screen, event)
        self.screen_manager.is_building_button_clicked(self.building_screen, event)
        self.screen_manager.is_serving_button_clicked(self.serving_screen, event)

        '''
        if self.ordering_screen.building_button_is_clicked(event):
            self.building_screen.make_current_screen()
            self.ordering_screen.end_current_screen()

        elif self.building_screen.blending_button_is_clicked(event):
            self.blending_screen.make_current_screen()
            self.building_screen.end_current_screen()

        elif self.blending_screen.topping_button_is_clicked(event):
            self.topping_screen.make_current_screen()
            self.blending_screen.end_current_screen()

        elif self.topping_screen.serving_button_is_clicked(event):
            self.serving_screen.make_current_screen()
            self.topping_screen.end_current_screen()'''

    def on_loop(self):
        pass

    def on_render(self):
        if self.ordering_screen.is_current:
            self.ordering_screen.update_display()

        if self.building_screen.is_current:
            self.building_screen.update_display()

        if self.blending_screen.is_current:
            self.blending_screen.update_display()

        if self.topping_screen.is_current:
            self.topping_screen.update_display()

        if self.serving_screen.is_current:
            self.serving_screen.update_display()

        '''if self.blending_screen.is_current:
            self.blending_screen.update_display()
        if self.topping_screen.is_current:
            self.topping_screen.update_display
        if self.serving_screen.is_current:
            self.serving_screen.update_display'''

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