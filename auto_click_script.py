from pynput import mouse, keyboard
import time
from pynput.keyboard import Key, KeyCode
import threading
from logging import info, basicConfig, INFO

# Configuration
TOGGLE_KEY = keyboard.Key.f6  # Hotkey to start/stop the auto-clicker
STOP_KEY = keyboard.Key.f7 # Hotkey to exit the program
CLICK_BUTTON = mouse.Button.right # Mouse button to click
CLICK_INTERVAL = 3  # Time in seconds between clicks

# Global state
clicking = False # clicking status
is_stop = False # ending status

def setup_logger()-> None:
    """
    Configures global logging behavior for the application.

    This function sets the logging level to INFO and defines a consistent message format
    for all log outputs. The log format includes a timestamp, the log level name, and
    the actual message. This setup helps ensure that logs are easy to read and debug,
    particularly during development or runtime diagnostics.

    Returns
    -------
    None
        This function does not return any value.
    """
    basicConfig(
        level=INFO,
        format='[%(asctime)s] %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )

def readable_key(key):
    if isinstance(key, Key):
        return key.name.upper()
    elif isinstance(key, KeyCode):
        return key.char.upper()
    return str(key)
        

def clicker_thread():
    """Function to perform clicks while 'clicking' is True."""
    global is_stop, clicking, keyboard_listener
    while not is_stop:
        if clicking:
            mouse_controller.click(CLICK_BUTTON)
            elapsed = 0.0
            step = 0.5

            # Wait in small increments (step) until the total elapsed time reaches the click_interval,
            # while continuously checking if the program should stop or if auto-clicking is still active.
            while elapsed < CLICK_INTERVAL and not is_stop and clicking:
                time.sleep(step)
                elapsed += step
        else:
            time.sleep(0.1) # Small delay to prevent busy-waiting
        
    # if exit command is activated
    keyboard_listener.stop() # Stop the keyboard listener
        

def on_press(key):
    """Callback for keyboard press events."""
    global clicking, is_stop
    if key == TOGGLE_KEY:
        clicking = not clicking
        if clicking:
            is_stop = False
            info("Auto-clicker started.")
        else:
            info("Auto-clicker stopped.")
    if key == STOP_KEY:
        is_stop = True
        info("Trying to Exit the Program.")
    
# Initialize controllers
mouse_controller = mouse.Controller()

# Set up keyboard listener in a non-blocking manner
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()
setup_logger()
info(f"Press {readable_key(TOGGLE_KEY)} to Start/Stop the Auto-Clicker.")
info(f"Press {readable_key(STOP_KEY)} to Exit the Program.")

# Start the clicker thread
click_thread = threading.Thread(target=clicker_thread, daemon=True) # (deamon=True) Allow the program to exit even if this thread is running
click_thread.start()

# Keep the main thread alive to listen for events
keyboard_listener.join()
info("2 threads are killed.")
info("The Auto-Clicker Program has ended.")