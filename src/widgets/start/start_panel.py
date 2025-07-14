from textual.containers import Container, Horizontal
from src.core.app_state.state import State
from src.widgets.start.configs_panel import ConfigsPanel
from src.widgets.start.runtime_panel import RuntimePanel
from textual.app import ComposeResult
from src.core.event.event_system import EventSystem

class StartPanel(Container):
    def __init__(
        self, 
        *children, 
        name = None, 
        id = None, 
        classes = None, 
        disabled = False, 
        markup = True, 
        state: State,
        events: EventSystem
    ):
        super().__init__(*children, name=name, id=id, classes=classes, disabled=disabled, markup=markup)
        self.state = state
        self.events = events
    
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield ConfigsPanel(state=self.state)
            yield RuntimePanel(state=self.state, events=self.events)
