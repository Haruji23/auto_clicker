from textual.widget import Widget
from src.core.app_state.state import State
from textual.widgets import Label, ListView, ListItem
from textual.app import ComposeResult
from logging import debug, getLogger
from src.core.event.event_system import EventSystem, RoutedEvent

class RuntimePanel(Widget):
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
        self._events = events
        self.logger = getLogger("AutoClicker")

    def compose(self) -> ComposeResult:
        self.list_view = ListView(
            id="runtime-list"
        )
        self.list_view.border_title = "Runtime Status"
        yield self.list_view
    
    def sync_keyboard_listening(self, is_on: bool):
        if not is_on:
            self.post_message(RoutedEvent(target="screen.start.listener_stop", payload={"status": "keyboard_listener stopped"}))
            self.logger.debug("Sent post_message ListenerStop")
        keyboard_listening_display = "[bold cyan]Keyboard Listener[/]: [bold italic ansi_bright_green]ON[/]" if is_on else "[bold cyan]Keyboard Listener[/]: [bold italic ansi_bright_red]OFF[/]"
        self.query_one("#keyboard-status").update(keyboard_listening_display)
    
    def sync_operating(self, is_on: bool):
        operating_display = "[bold yellow]Clicker[/]: [bold italic ansi_bright_green]ON[/]" if is_on else "[bold yellow]Clicker[/]: [bold italic ansi_bright_red]OFF[/]"
        self.query_one("#clicking-status").update(operating_display)
        
    def on_mount(self):
        self.logger.debug("RuntimePanel on_mount() is triggered")
        keyboard_listening_display = "[bold cyan]Keyboard Listener[/]: [bold italic ansi_bright_green]ON[/]" if self.state.keyboard_listening else "[bold cyan]Keyboard Listener[/]: [bold italic ansi_bright_red]OFF[/]"
        self.list_view.append(ListItem(Label(keyboard_listening_display, markup=True, id="keyboard-status")))
        operating_display = "[bold yellow]Clicker[/]: [bold italic ansi_bright_green]ON[/]" if self.state.operating else "[bold yellow]Clicker[/]: [bold italic ansi_bright_red]OFF[/]"
        self.list_view.append(ListItem(Label(operating_display, markup=True, id="clicking-status")))
        self.logger.debug(f"RuntimePanel ListView children count: {len(self.list_view.children)}")
        self._events.register_observer("keyboard_listening", self.sync_keyboard_listening)
        self._events.register_observer("operating", self.sync_operating)
    
    def on_unmount(self):
        self._events.unregister_observer("operating")
        self._events.unregister_observer("keyboard_listening")