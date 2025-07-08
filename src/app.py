from textual.app import App
from src.screens.menu import MenuScreen
from src.screens.start import StartScreen
from src.core.state import State

class AutoClickerApp(App):
    def __init__(
            self, 
            driver_class = None, 
            css_path = None,
            watch_css = False,
            ansi_color = False, 
            state: State | None = None
    ):
        super().__init__(driver_class, css_path, watch_css, ansi_color)
        self.state = state
    
    # SCREENS = {
    #     "menu": MenuScreen,
    #     "start": StartScreen
    # }

    def on_mount(self) -> None:
        self.push_screen(screen=MenuScreen(state=self.state)) # Start with Menu Screen
