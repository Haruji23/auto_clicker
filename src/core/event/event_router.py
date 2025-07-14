from textual.message import Message
from logging import error
from typing import Callable
from logging import debug

class RoutedEvent(Message):
    def __init__(self, target: str, payload: dict | None = None) -> None:
        super().__init__()
        self.target = target
        self.payload = payload or {}

class EventRouter:
    def __init__(self):
        self.routes: dict[str, Callable] = {}

    def register(self, name: str, handler: Callable):
        if name not in self.routes:
            self.routes[name] = handler
        else:
            debug(f"[EventTrace] [Register] [EventRouter] Target Already Exist: {name}")
    
    def unregister(self, name: str):
        if name in self.routes:
            del self.routes[name]
        else:
            debug(f"[EventTrace] [Register] [EventRouter] Target Not Exist: {name}")


    def dispatch(self, event: RoutedEvent):
        handler = self.routes[event.target]
        if handler:
            debug(f"[EventTrace] [Dispatch] [EventRouter] {handler.__name__}, payload= {event.payload}")
            handler(event.payload)
        else:
            error(f"[EventTrace] [Dispatch] [EventRouter] No handler for target: {event.target}")
