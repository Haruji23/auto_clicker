from textual.app import App
from src.screens.menu import MenuScreen
from src.core.app_state.state import State, state
from logging import debug

class AutoClickerApp(App):
    def __init__(
        self, 
        driver_class = None, 
        css_path = None,
        watch_css = False,
        ansi_color = False, 
        state: State = state
    ):
        super().__init__(driver_class, css_path, watch_css, ansi_color)
        self.state = state
    
    # SCREENS = {
    #     "menu": MenuScreen,
    #     "start": StartScreen
    # }

    def on_mount(self) -> None:
        debug(f"State in AutoClickerApp: {self.state.app_state_dict()}")
        self.push_screen(screen=MenuScreen(state=self.state)) # Start with Menu Screen
