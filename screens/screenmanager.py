
class ScreenManager:
    def __init__(self):
        self.cur_screen = None

    def is_blending_button_clicked(self, blending_screen, event):
        if self.cur_screen.blending_button_is_clicked(event):
            blending_screen.make_current_screen()
            self.cur_screen.end_current_screen()
            self.cur_screen = blending_screen

