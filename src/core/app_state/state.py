"""
Shared state object for managing the auto-clicker's runtime behavior.

This module defines the `State` class, which acts as a central data pool
during the program's execution. It holds user-defined configurations
(e.g., hotkeys, click interval, mouse button) as well as volatile runtime flags,
such as whether the clicker is currently active or should terminate.

Classes:
    State: Stores the current config and runtime state flags.
"""

from dataclasses import dataclass, field
from typing import Callable
from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button
from src.utils.key_parser import key_mouse_to_str, parse_key, parse_button
@dataclass
class State:
    """
    Represents the runtime state and user-defined configurations of the auto-clicker.

    Attributes:
        operating (bool) : Whether the auto-clicker is currently running
        exiting (bool): Whether the application is in the process of exiting.
        toggle_key (Key | KeyCode): Keyboard shortcut to start or stop the auto-clicker.
        exit_key (Key | KeyCode) : Keyboard shortcut to trigger application shutdown.
        click_button (Button): The mouse button used for clicking (e.g., Button.left, Button.right, Button.middle).
        click_interval (float): Delay in seconds between mouse clicks.
    """

    # Applicaion State
    _operating: bool = False
    _exiting: bool = False
    _keyboard_listening: bool = False
    # observers: dict[str, list[Callable]] = field(default_factory=lambda: {
    #     "operating": [],
    #     "keyboard_listening": [],
    #     "exiting": []
    # })
    
    # Configurations
    toggle_key: Key | KeyCode = Key.f6 # Hotkey to start/stop the auto-clicker (default = F6)
    exit_key: Key | KeyCode = Key.f8 # Hotkey to exit the program (default = F8)
    click_button: Button = Button.right # Mouse button to click (default = right)
    click_interval: float = 60.0 # Time in seconds between click (default = 60.0)
    
    # def register(self, key: str, callback: Callable):
    #     if key in self.observers:
    #         self.observers[key].append(callback)

    # def unregister(self, key: str, callback: Callable):
    #     if key in self.observers and callback in self.observers[key]:
    #         self.observers[key].remove(callback)
    
    @property
    def operating(self):
        return self._operating

    @operating.setter
    def operating(self, value: bool):
        self._operating = value
        # if value != self._operating:
        #     self._operating = value
        #     for cb in self.observers["operating"]:
        #         cb(value)
    
    @property
    def keyboard_listening(self):
        return self._keyboard_listening

    @keyboard_listening.setter
    def keyboard_listening(self, value: bool):
        self._keyboard_listening = value
        # if value != self._keyboard_listening:
        #     self._keyboard_listening = value
        #     for cb in self.observers["keyboard_listening"]:
        #         cb(value)
    
    @property
    def exiting(self):
        return self._exiting

    @exiting.setter
    def exiting(self, value: bool):
        self._exiting = value
        # if value != self._exiting:
        #     self._exiting = value
        #     for cb in self.observers["exiting"]:
        #         cb(value)

    @property
    def toggle_key_str(self) -> str:
        """
        Returns the string representation of the toggle key.

        Returns:
            str: Readable hotkey name (e.g., "F6").
        """
        return key_mouse_to_str(self.toggle_key)

    @property
    def exit_key_str(self) -> str:
        """Return the string representation of the stop key.

        Returns:
            str: Readable hotkey name (e.g., "F8").
        """
        return key_mouse_to_str(self.exit_key)
    @property
    def click_button_str(self) -> str:
        """
        Return the string representation of the mouse button.

        Returns:
            str : Readable mouse button (e.g., right)
        """
        return key_mouse_to_str(self.click_button)
    
    def set_data_from_dict(self, data: dict) -> None:
        """
        Sets the data from a dict. (toggle_key, exit_key, click_button, click_interval)

        Parameters:
            data (dict): Data is loaded from a json file.
        
        Returns:
            None: This method does not return a value.
        """
        self.toggle_key = parse_key(data["toggle_key"])
        self.exit_key = parse_key(data["exit_key"])
        self.click_button = parse_button(data["button"])
        self.click_interval = data["interval"]
    
    def raw_configs_dict(self)-> dict:
        """
        Converts the configurations to a dictionary.(Ureadable form)
        
        Returns:
            dict : Dictionary of configurations, but unreadable form. 
        """
        data = {
            "toggle_key": self.toggle_key,
            "exit_key": self.exit_key,
            "button": self.click_button,
            "interval": self.click_interval
        } 
        return data
    
    def configs_dict(self) -> dict:
        """
        Converts the configurations to a dictionary.(Readable form)
        
        Returns:
            dict : Dictionary of configurations, and readable form.
        """
        data = {
            "toggle_key": self.toggle_key_str,
            "exit_key": self.exit_key_str,
            "button": self.click_button_str,
            "interval": self.click_interval
        }
        return data
    
    def app_state_dict(self) -> dict:
        data = {
            "operating": self.operating,
            "exiting": self.exiting,
            "keyboard_listening": self.keyboard_listening,
            # "observers": self.observers
        }
        return data

state = State()