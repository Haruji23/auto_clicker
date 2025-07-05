"""
Keyboard listener logic for toggle and exit hotkeys.

Defines the `create_on_press()` callback that responds to user key input.

Args:
    state (State) : Class containing clicker setting & program status
"""

from core.state import State
from logging import info, debug
from typing import Callable
from pynput.keyboard import Key, KeyCode

def create_on_press(state: State) -> Callable[[Key, KeyCode], None]:
    """
    Returns a keyboard event handler that controls the auto-clicker's runtime behavior.

    This function generates a callback function (`on_press`) that listens for specific key inputs.
    When the toggle key is pressed, it flips the operating state of the auto-clicker. When the
    stop key is pressed, it marks the application for termination.

    Parameters:
        state (State): An instance of the State class containing runtime flags and user-defined hotkeys.

    Returns:
        Callable[[Key | KeyCode], None]: A handler function used with pynput listener.
    """

    def on_press(key: Key | KeyCode) -> None:
        """
        Callback function triggered whenever a key is pressed.

        This function checks if the pressed key matches the toggle or stop key defined in the shared
        state object. If the toggle key is pressed, the auto-clicker switches between active and
        inactive states. If the stop key is pressed, it signals the application to exit gracefully.

        Side Effects:
        - Sets or unsets `state.operating`, changing whether the clicker is actively clicking.
        - Sets `state.exiting = True` to trigger application shutdown on the next cycle.
        - Emits logging messages indicating mode transitions.

        Parameters:
            key (Key | KeyCode): The key object received from pynput's keyboard listener. Can be a special key (Key) or a character key (KeyCode).

        Returns:
            None: This function performs state transitions and logging, but does not return a value.
        """
        if key == state.toggle_key:
            state.operating = not state.operating
            debug(f"Operating's state : {state.operating}")
            if state.operating:
                info("[bold cyan]Auto-clicker[/] [bold green]started.[/]")
            else:
                info("[bold cyan]Auto-clicker[/] [bold red]stopped.[/]")
        if key == state.exit_key:
            state.exiting = True
            debug(f"Exiting's state: {state.exiting}")
            info("Trying to [bold red]exit[/] the program.")
    return on_press