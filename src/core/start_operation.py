from core.state import State
from logging import info
from pynput.keyboard import Listener
from pynput.mouse import Controller
from core.clicker import AutoClicker
from core.on_press import create_on_press

"""
Entry point to launch the auto-clicker loop.

Loads configuration, displays current state, and starts the clicker thread.

Args:
    state (State) : Class containing user-defined configurations & runtime status
"""


def start_auto_clicker(state: State) -> None:
    """
    This function shared application state, mouse controller,
    hotkey listener, and auto-clicker thread. It starts the key listener and
    background clicker, then blocks until termination is triggered via the stop hotkey.

    Returns:
        None: This function does not return any value.
    """
    # Initialize a controller
    mouse_controller = Controller()

    # Set up keyboard listener in a non-blocking manner
    keyboard_listener = Listener(on_press=create_on_press(state=state))

    # Initailize an auto-click thread
    auto_clicker = AutoClicker(
        mouse_controller=mouse_controller,
        keyboard_listener=keyboard_listener,
        state=state
    )
    # Start the keyboard listener
    keyboard_listener.start()
    
    # Start the auto clicker thread
    auto_clicker.start()
    
    # Keep the main thread alive to listen for events
    keyboard_listener.join()

    info("[bold cyan]Auto-Clicker[/] thread [bold red]stopped.[/]")
    info("[magenta]2[/] threads [bold red]were killed.[/]")
    info("[bold cyan]Auto-Clicker[/] Program [bold red]has ended.[/]")