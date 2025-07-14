from textual.widgets import Footer, Header
from textual.screen import Screen
from src.widgets.menu.menu_buttons import MenuButtonPanel
from textual.app import ComposeResult
from src.core.app_state.state import State, state
from logging import debug, getLogger

class MenuScreen(Screen):

    def __init__(
        self, 
        name = "MenuScreen", 
        id = None, 
        classes = None,
        state: State = state
    ):
        super().__init__(name, id, classes)
        self.state = state
        self.logger = getLogger("AutoClicker")

    CSS_PATH = "../../assets/menu.tcss"
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield MenuButtonPanel(state=self.state)
        yield Footer()
    
    def on_mount(self):
        self.logger.debug(f"State in MenuScreen: {self.state.app_state_dict()}")
    