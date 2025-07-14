from textual.widget import Widget
from textual.app import ComposeResult
from textual.widgets import Label, ListView, ListItem
from src.core.app_state.state import State
from logging import debug, getLogger

class ConfigsPanel(Widget):

    def __init__(
        self, 
        *children, 
        name = "ConfigPanel", 
        id = None, 
        classes = None, 
        disabled = False, 
        markup = True, 
        state: State
    ):
        super().__init__(
            *children, 
            name=name, 
            id=id, 
            classes=classes, 
            disabled=disabled, 
            markup=markup
        )
        self.state = state
        self.logger = getLogger("AutoClicker")
    
    def compose(self) -> ComposeResult:
        self.list_view = ListView(id="configs-list")
        self.list_view.border_title = "Current Configurations"
        yield self.list_view

    def on_mount(self) -> None:
        self.logger.debug("ConfigsPanel on_mount() is triggered")
        config = self.state.configs_dict()
        for key, value in config.items():
            if key == "toggle_key":
                display = f"[bold cyan]Start/Stop Key[/]: [bold italic cyan]{value}[/]"
            elif key == "exit_key":
                display = f"[bold pink]Exit to Menu Key[/]: [bold italic pink]{value}[/]"
            elif key == "interval":
                display = f"[bold magenta]Time interval[/]: [bold italic magenta]{value}[/]"
            elif key == "button":
                display = f"[bold yellow]Mouse Button[/]: [bold italic yellow]{value}[/]"
            self.list_view.append(ListItem(Label(display, markup=True)))
        self.logger.debug(f"ConfigsPanel ListView children count: {len(self.list_view)}")