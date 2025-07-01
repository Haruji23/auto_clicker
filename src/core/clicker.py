from time import sleep
from threading import Thread
from pynput.keyboard import Listener
from pynput.mouse import Controller
from core.state import State
from logging import info

class AutoClicker(Thread):
    """
    A background thread that continuously performs automated mouse clicks
    based on the current state configuration.

    Attributes
    ----------
    keyboard_listener : pynput.keyboard.Listener
        A keyboard listener instance used to stop listening when exiting.
    mouse_controller : pynput.mouse.Controller
        A controller instance used to execute mouse click actions.
    state : State
        Shared state object containing runtime flags and click settings.

    Methods
    -------
    run():
        Executes the main auto-clicking loop, clicking at the specified interval
        as long as the operating flag is active and the program is not exiting.
    """

    def __init__(
                self,
                keyboard_listener: Listener,
                mouse_controller: Controller,
                state: State
                ):
        super().__init__(
            daemon=True, # Allow the program to exit even if this thread is running
            target=self.run 
            )
        self.mouse = mouse_controller
        self.keyboard_listener = keyboard_listener
        self.state = state

    def run(self) -> None:
        """
        Executes the main auto-clicking loop, performing mouse clicks at a defined
        interval while monitoring the state flags.

        Returns
        -------
        None
            This method does not return a value.
        """
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
        self.keyboard_listener.stop() # Stop running the keyboard listener
        info("[bold green]Keyboard listener[/] [bold red]stopped.[/]")
