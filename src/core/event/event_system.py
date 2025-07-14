from src.core.event.event_router import EventRouter, RoutedEvent
from src.core.event.state_observer import StateObserver
from src.core.event.event_logger import EventLogger
from src.core.app_state.state import State
from typing import Callable, Any

class EventSystem:
    def __init__(self, state: State):
        self.observer = StateObserver(state)
        self.router = EventRouter()
        self.logger = EventLogger()
        self.lifecycle: dict[str, Callable] = {}

    def register_observer(self, key: str, callback: Callable):
        self.logger.trace(f"[Observer] Registered: {key} → {callback.__name__}")
        self.observer.register(key, callback)
    
    def unregister_observer(self, key: str):
        self.logger.trace(f"[Observer] Unregister all callbacks: {key}")
        self.observer.unregister(key=key)
    
    def unregister_observer_callback(self, key: str, callback: Callable):
        self.logger.trace(f"[Observer] Unregister a callback: {key} → {callback.__name__}")
        self.observer.unregister_callback(key=key, callback=callback)

    def update_state(self, key: str, value: Any):
        self.logger.trace(f"[State] Updated: {key} = {value}")
        self.observer.set(key, value)

    def register_route(self, target: str, handler: Callable):
        self.logger.trace(f"[Router] Registered: {target} → {handler.__name__}")
        self.router.register(target, handler)

    def unregister_route(self, target: str):
        self.logger.trace(f"[Router] Registered: {target}")
        self.router.unregister(target)

    def dispatch(self, event: RoutedEvent):
        self.logger.trace(f"[Dispatch] RoutedEvent → {event.target}, payload={event.payload}")
        self.router.dispatch(event)

    def on_lifecycle(self, stage: str, callback: Callable):
        self.logger.trace(f"[Lifecycle] Hook: {stage} → {callback.__name__}")
        self.lifecycle[stage] = callback

    def trigger_lifecycle(self, stage: str):
        if stage in self.lifecycle:
            self.logger.trace(f"[Lifecycle] Triggered: {stage}")
            self.lifecycle[stage]()
        else:
            self.logger.warn(f"[Lifecycle] No hook for: {stage}")
