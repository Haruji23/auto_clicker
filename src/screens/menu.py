from textual.widgets import Footer, Header
from textual.screen import Screen
from src.widgets.menu_buttons import MenuButtonPanel
from textual.app import ComposeResult
from src.core.state import State

class MenuScreen(Screen):

    def __init__(
        self, 
        name = "MenuScreen", 
        id = None, 
        classes = None,
        state: State | None = None
    ):
        super().__init__(name, id, classes)
        self.state = state

    CSS_PATH = "../../assets/menu.tcss"
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield MenuButtonPanel(state=self.state)
        yield Footer()
    