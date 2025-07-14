from textual.widgets import Footer, Header
from textual.screen import Screen
from src.widgets.start.start_panel import StartPanel
from src.core.app_state.state import State
from textual.app import ComposeResult
from src.core.start_operation import start_auto_clicker
from src.utils.to_menu import switch_to_menu
from logging import debug, info, getLogger
from src.core.event.event_router import RoutedEvent
from src.core.event.event_system import EventSystem

class StartScreen(Screen):
    CSS_PATH = "../../assets/start.tcss"
    
    def __init__(
        self, 
        name = "StartScreen", 
        id = None, 
        classes = None, 
        state: State | None = None
    ):
        super().__init__(name, id, classes)
        self.state = state
        self._exit_event = False
        self._listener_stop_event = False
        self._menu_returned = False
        self._events = EventSystem(state=state)
        self.logger = getLogger("AutoClicker")

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield StartPanel(state=self.state, events=self._events)
        yield Footer()
    
    def on_mount(self):
        self._events.register_observer("exiting", self.exit_triggered)
        self._events.register_route("screen.start.listener_stop", self.listener_stop)
        self._events.register_route("screen.start.exit_to_menu", self.exit_to_menu)
        start_auto_clicker(state=self.state, events=self._events)
        self.logger.debug(f"State in StartScreen(Before): {self.state.app_state_dict()}")
    
    def on_unmount(self):
        self._events.update_state("exiting", False)
        self._events.unregister_observer("exiting")
        self._events.unregister_route("screen.start.listener_stop")
        self._events.unregister_route("screen.start.exit_to_menu")
        self.logger.debug(f"State in StartScreen(After): {self.state.app_state_dict()}")

    # def on_routed_event(self, event: RoutedEvent):
    #     self.router.dispatch(event)

    def on_routed_event(self, event: RoutedEvent):
        self._events.dispatch(event)

    def exit_triggered(self, value: bool):
        if value:
            self.post_message(RoutedEvent("screen.start.exit_to_menu", payload={"reason": "exit_key"})) # send event to main thread
            self.logger.debug("Sent post_message ExitToMenu")
    
    def exit_to_menu(self, payload: dict):
        if payload["reason"] == "exit_key":
            self._exit_event = True
            info("[StartScreen] Receive Exit To Menu Event")
            self._try_return_to_menu()

    def listener_stop(self, payload: dict):
        if payload["status"] == "keyboard_listener stopped":
            self._listener_stop_event = True
            info("[StartScreen] Receive Keyboard Listener Stopped Event")
            self._try_return_to_menu()
    
    def _try_return_to_menu(self):
        if self._listener_stop_event and self._exit_event and not self._menu_returned:
            self._menu_returned = True
            self.logger.debug("[StartScreen] Both events received. Returning to Menu.")
            self.app.pop_screen()
            switch_to_menu(app=self.app, state=self.state)
