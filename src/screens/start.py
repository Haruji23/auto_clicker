from textual.widgets import Footer, Header
from textual.screen import Screen
from src.widgets.configs_panel import ConfigsPanel
from src.core.state import State
from textual.app import ComposeResult


class StartScreen(Screen):
    CSS_PATH = "../../assets/configs.tcss"
    
    def __init__(
        self, 
        name = None, 
        id = None, 
        classes = None, 
        state: State | None = None
    ):
        super().__init__(name, id, classes)
        self.state = state

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield ConfigsPanel(state=self.state)
        yield Footer()