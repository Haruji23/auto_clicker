from textual.widget import Widget
from textual.app import ComposeResult
from src.config.load import load_configs
from src.config.constants import CONFIGS_PATH
from textual.widgets import Label, ListView, ListItem
from src.core.state import state, State

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
    
    def compose(self) -> ComposeResult:
        self.list_view = ListView(id="configs-list")
        self.list_view.border_title = "Current Configurations"
        yield self.list_view

    def on_mount(self) -> None:
        config = self.state.to_show_dict()
        for key, value in config.items():
            if key == "toggle_key":
                display = f"[italic cyan]{key}[/]: [bold cyan]{value}[/]"
            elif key == "exit_key":
                display = f"[italic pink]{key}[/]: [bold pink]{value}[/]"
            elif key == "interval":
                display = f"[italic orange]{key}[/]: [bold orange]{value}[/]"
            elif key == "button":
                display = f"[italic yellow]{key}[/]: [bold yellow]{value}[/]"
            self.list_view.append(ListItem(Label(display, markup=True)))