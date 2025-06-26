from pynput import mouse, keyboard
import time
import threading

# Configuration
TOGGLE_KEY = keyboard.Key.f6  # Hotkey to start/stop the auto-clicker
STOP_KEY = keyboard.Key.f7 # Hotkey to exit the program
CLICK_BUTTON = mouse.Button.right # Mouse button to click
CLICK_INTERVAL = 3  # Time in seconds between clicks

# Global state
clicking = False # clicking status
is_stop = False # ending status

def clicker_thread():
    """Function to perform clicks while 'clicking' is True."""
    global is_stop, clicking, keyboard_listener
    while True:
        if is_stop:
            keyboard_listener.stop() # Stop the keyboard listener
            break # Stop the clicker thread
        elif clicking:
            mouse_controller.click(CLICK_BUTTON)
            time.sleep(CLICK_INTERVAL)
        else:
            time.sleep(0.1) # Small delay to prevent busy-waiting

def on_press(key):
    """Callback for keyboard press events."""
    global clicking, is_stop
    if key == TOGGLE_KEY:
        clicking = not clicking
        if clicking:
            is_stop = False
            print("Auto-clicker started.")
        else:
            print("Auto-clicker stopped.")
    if key == STOP_KEY:
        is_stop = True
        print(f"is_stop = {is_stop}")
    

# Initialize controllers
mouse_controller = mouse.Controller()

# Set up keyboard listener in a non-blocking manner
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Start the clicker thread
click_thread = threading.Thread(target=clicker_thread)
click_thread.daemon = True # Allow the program to exit even if this thread is running
click_thread.start()

# Keep the main thread alive to listen for events
keyboard_listener.join()
print("2 threads are killed.")
print("The Auto-Clicker Program has ended.")