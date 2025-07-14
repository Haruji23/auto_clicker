from pynput.keyboard import Listener
from logging import info, getLogger
from src.core.app_state.state import State
from typing import Callable
from time import sleep
from src.core.event.event_system import EventSystem

class ListenerManager:
    def __init__(self, state: State, callback: Callable, events: EventSystem):
        self.listener = Listener(on_press=callback)
        self.state = state
        self.events = events
        self.logger = getLogger("AutoClicker")

    def start(self):
        if not self.listener or not self.listener.running:
            self.listener.start()
            self.listener._thread.name = "KeyboardListenerThread"
            if self.listener.running:
                self.events.update_state("keyboard_listening", True)
                self.logger.info(f"[{self.listener._thread.name}] has started")
        elif self.listener.running:
            self.logger.info(f"[{self.listener._thread.name}] is still running - skip starting")

    def stop_async(self):
        if self.listener and self.listener.running:
            self.listener.stop()
            while self.listener.running:
                sleep(0.1)
            # if listener not running
            self.logger.info(f"[{self.listener._thread.name}] stopped")
            self.events.update_state("keyboard_listening", False)