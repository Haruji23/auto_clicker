from dataclasses import dataclass
from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button
from utils.key_parser import key_mouse_to_str, parse_key, parse_button
@dataclass
class State:
    """
    Represents the runtime state and configuration of the auto-clicker.

    Attributes
    ----------
    operating : bool
        Whether the auto-clicker is actively running (i.e., clicking).
    exiting : bool
        Whether the application is in the process of exiting.
    toggle_key : Key | KeyCode
        Keyboard shortcut to start or stop the auto-clicker.
    exit_key : Key | KeyCode
        Keyboard shortcut to trigger application shutdown.
    click_button : Button
        The mouse button used for clicking (e.g., Button.left or Button.right).
    click_interval : float
        Delay in seconds between mouse clicks.
    """

    # Applicaion State
    operating: bool = False
    exiting: bool = False

    # Configurations
    def __init__(self,
                toggle_key: Key | KeyCode = Key.f6, # Hotkey to start/stop the auto-clicker (default = F6)
                exit_key: Key | KeyCode = Key.f8, # Hotkey to exit the program (default = F8)
                click_button: Button = Button.right, # Mouse button to click (default = right)
                click_interval: float = 60.0 # Time in seconds between click (default = 60.0)
                )-> None:
        self.toggle_key = toggle_key
        self.exit_key = exit_key
        self.click_button = click_button
        self.click_interval = click_interval

    @property
    def toggle_key_str(self) -> str:
        """
        Returns the string representation of the toggle key.

        Returns
        -------
        string
            Readable hotkey name (e.g., "F6").
        """
        return key_mouse_to_str(self.toggle_key)

    @property
    def exit_key_str(self) -> str:
        """
        Returns the string representation of the stop key.

        Returns
        -------
        str
            Readable hotkey name (e.g., "F8").
        """
        return key_mouse_to_str(self.exit_key)
    @property
    def click_button_str(self) -> str:
        """
        Return the string representation of the mouse button.

        Returns
        -------
        str
            Readable mouse button (e.g., right)
        """
        return key_mouse_to_str(self.click_button)
    
    def set_data_from_dict(self, data: dict) -> None:
        """
        Sets the data from a dict. (toggle_key, exit_key, click_button, click_interval)

        Parameter
        data : dictionary
            Data is loaded from a json file
        
        Returns
        -------
        None
            This method does not return a value.
        """
        self.toggle_key = parse_key(data["toggle_key"])
        self.exit_key = parse_key(data["exit_key"])
        self.click_button = parse_button(data["button"])
        self.click_interval = data["interval"]
    
    def to_dict(self)-> dict:
        """
        Converts the configurations to a dictionary.(Ureadable form)
        
        Returns
        -------
        dict
            Dictionary of configurations, but unreadable form.
        
        """
        data = {
            "toggle_key": self.toggle_key,
            "exit_key": self.exit_key,
            "button": self.click_button,
            "interval": self.click_interval
        } 
        return data
    
    def to_show_dict(self) -> dict:
        """
        Converts the configurations to a dictionary.(Readable form)
        
        Returns
        -------
        dict
            Dictionary of configurations, and readable form.
        
        """
        data = {
            "toggle_key": self.toggle_key_str,
            "exit_key": self.exit_key_str,
            "button": self.click_button_str,
            "interval": self.click_interval
        }
        return data