from textual.widget import Widget
from textual.widgets import Button, Label
from textual.containers import Vertical
from textual.app import ComposeResult
from src.core.state import State
from src.screens.start import StartScreen


class MenuButtonPanel(Widget):
    """A vertical group of menu buttons for navigation."""

    def __init__(self, *children, name = None, id = None, classes = None, disabled = False, markup = True, state: State):
        super().__init__(*children, name=name, id=id, classes=classes, disabled=disabled, markup=markup)
        self.state = state

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Tip: Navigate using [bold cyan]Tab[/] and press [bold cyan]Enter[/] to select.\n[bold cyan]Mouse clicks[/] work too!", id="menu-hint"),
            Button("Start", id="start", classes="menu", variant="success"),
            Button("Settings", id="settings", classes="menu", variant="default"),
            Button("Exit", id="exit", classes="menu", variant="error"),
            id="menu-buttons",
            markup=True
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "start":
                self.app.push_screen(StartScreen(state=self.state))
            # case "settings":
            #     self.app.push_screen("settings")
            case "exit":
                self.app.exit()