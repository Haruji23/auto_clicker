from pynput.keyboard import Listener
from pynput.mouse import Controller
from on_press import create_on_press
from clicker import AutoClicker
from logging import info
from setup_logger import setup_logger
from state import State

def main() -> None:
    """
    Entry point for the auto-clicker program.

    This function initializes the logger, shared application state, mouse controller,
    hotkey listener, and auto-clicker thread. It starts the key listener and
    background clicker, then blocks until termination is triggered via the stop hotkey.

    Returns
    -------
    None
        This function does not return any value.
    """

    # Call setup_logger function to config logging
    setup_logger()

    # Initialize a controller
    mouse_controller = Controller()

    # Initialize a state of program (data pool)
    state = State()

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

    # Show the Start/Stop key, and Exit key
    info(f"Press {state.toggle_key_str} to Start/Stop Auto-Clicker")
    info(f"Press {state.exit_key_str} to Exit the program")
    
    # Start the auto clicker thread
    auto_clicker.start()
    
    # Keep the main thread alive to listen for events
    keyboard_listener.join()

    info("Auto-Clicker thread stopped")
    info("2 threads were killed.")
    info("Auto-Clicker Program has ended.")


if __name__ == "__main__":
    main()