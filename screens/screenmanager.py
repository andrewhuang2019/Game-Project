
class ScreenManager:
    def __init__(self):
        self.cur_screen = None

    def is_building_button_clicked(self, building_screen, event):
        if self.cur_screen.building_button_is_clicked(event):
            building_screen.make_current_screen()
            self.cur_screen.end_current_screen()
            self.cur_screen = building_screen

    def is_blending_button_clicked(self, blending_screen, event):
        if self.cur_screen.blending_button_is_clicked(event):
            blending_screen.make_current_screen()
            self.cur_screen.end_current_screen()
            self.cur_screen = blending_screen
    
    def is_topping_button_clicked(self, topping_screen, event):
        if self.cur_screen.topping_button_is_clicked(event):
            topping_screen.make_current_screen()
            self.cur_screen.end_current_screen()
            self.cur_screen = topping_screen
    
    def is_ordering_button_clicked(self, ordering_screen, event):
        if self.cur_screen.ordering_button_is_clicked(event):
            ordering_screen.make_current_screen()
            self.cur_screen.end_current_screen()
            self.cur_screen = ordering_screen
    
