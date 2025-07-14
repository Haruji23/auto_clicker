from src.core.app_state.state import State
from typing import Callable, Any
from logging import debug

class StateObserver:
    def __init__(self, state: State):
        self.state = state
        self.callbacks: dict[str, set[Callable]] = {}
    
    def register(self, key: str, callback: Callable):
        if key not in self.callbacks:
            self.callbacks[key] = set()
            self.callbacks[key].add(callback)
        else:
            debug(f"{key} already existed in StateObserver")

    def unregister(self, key: str):
        if key in self.callbacks:
            del self.callbacks[key]
        else:
            debug(f"No {key} in StateObserver")
    
    def unregister_callback(self, key: str, callback: Callable):
        if key in self.callbacks and callback in self.callbacks[key]:
            self.callbacks[key].discard(callback)
    
    def notify(self, key: str, value: Any):
        if key in self.callbacks:
            for callback in self.callbacks[key]:
                callback(value)
        else:
            debug(f"No {key} in StateObserver")
        
    def set(self, key: str, value: Any):
        setattr(self.state, key, value)
        self.notify(key=key, value=value)