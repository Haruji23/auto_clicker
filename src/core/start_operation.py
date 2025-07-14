from src.core.app_state.state import State
from logging import info
from pynput.keyboard import Listener
from pynput.mouse import Controller
from src.core.clicker import AutoClicker
from src.core.keyboard_listener.on_press import create_on_press
from logging import debug
from src.core.keyboard_listener.key_listen_manager import ListenerManager
from src.core.event.event_system import EventSystem

"""
Entry point to launch the auto-clicker loop.

Loads configuration, displays current state, and starts the clicker thread.

Args:
    state (State) : Class containing user-defined configurations & runtime status
"""


def start_auto_clicker(state: State, events: EventSystem) -> None:
    """
    This function shared application state, mouse controller,
    hotkey listener, and auto-clicker thread. It starts the key listener and
    background clicker, then blocks until termination is triggered via the stop hotkey.

    Returns:
        None: This function does not return any value.
    """
    # Initialize a controller
    mouse_controller = Controller()

    # Set up keyboard listener
    keyboard_listener = ListenerManager(
        state=state, 
        callback=create_on_press(
            state=state,
            events=events
        ),
        events=events
    )

    # Start the keyboard listener
    keyboard_listener.start()
    
    # Initailize an auto-click thread
    auto_clicker = AutoClicker(
        mouse_controller=mouse_controller,
        keyboard_listener=keyboard_listener,
        state=state,
    )

    # Start the auto clicker thread
    auto_clicker.start()
