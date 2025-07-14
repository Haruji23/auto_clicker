"""
Threaded auto-clicker logic.

Defines the AutoClicker class that performs mouse clicks at a given interval
until toggled off.

Classes:
    AutoClicker: A daemon thread that performs repeated mouse clicks.
"""

from time import sleep
from threading import Thread
from src.core.keyboard_listener.key_listen_manager import ListenerManager
from pynput.mouse import Controller
from src.core.app_state.state import State
from logging import info, debug

class AutoClicker(Thread):
    """
    A background thread that continuously performs automated mouse clicks
    based on the current state configuration.

    This thread activates mouse clicks at regular intervals as long as the
    auto-clicker is toggled on and the application has not been marked for exit.

    Attributes:
        keyboard_listener (pynput.keyboard.Listener): A keyboard listener instance
            used to stop listening when the program exits.
        mouse_controller (pynput.mouse.Controller): A controller used to simulate mouse clicks.
        state (State): An object containing runtime flags and user-defined config.

    Methods:
        run(): Executes the auto-click loop until the stop condition is triggered.
    """


    def __init__(
        self,
        keyboard_listener: ListenerManager,
        mouse_controller: Controller,
        state: State
    ):
        super().__init__(
            daemon=True, # Allow the program to exit even if this thread is running
            target=self.run,
            name="ClickerThread" # Name the thread as ClickerThread
        )
        self.mouse = mouse_controller
        self.keyboard_listener = keyboard_listener
        self.state = state

    def run(self) -> None:
        """
        Executes the main auto-clicking loop, performing mouse clicks at a defined
        interval while monitoring the state flags.

        Returns:
            None: This method does not return a value.
        """
        debug(f"{self.name} has been activated")
        while not self.state.exiting: # while program's running
            if self.state.operating: # if auto-clicking's acitived
                self.mouse.click(self.state.click_button)
                elapsed = 0.0
                step = 0.5

                # Wait in small increments (step) until the total elapsed time reaches the click_interval,
                # while continuously checking if the program should stop or if auto-clicking is still active.
                while elapsed < self.state.click_interval and not self.state.exiting and self.state.operating:
                    sleep(step)
                    elapsed += step
            else:
                sleep(0.1)
        # if exiting is true
        debug(f"Exiting's state: {self.state.exiting}")
        self.keyboard_listener.stop_async() # Stop running the keyboard listener
        info("Keyboard listener stopped.")
        debug(f"Keyboard listening: {self.state.keyboard_listening}")