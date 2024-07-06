
class ScreenManager:
    def __init__(self):
        self.screens = {}
        self.cur_screen = None
    
    def add_screen(self, name, screen):
        self.screens[name] = screen
    
    def set_screen(self, name):
        self.cur_screen = self.screens.get(name)
    
    def handle_events(self, events):
        if self.cur_screen:
            self.cur_screen.handle_events(events)
    
    def update(self):
        if self.cur_screen:
            self.cur_screen.update()
    
    def draw(self, screen):
        if self.cur_screen:
            self.cur_screen.draw(screen)

class Screen:
    def __init__(self, manager):
        self.manager = manager 

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass