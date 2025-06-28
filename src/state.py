from dataclasses import dataclass
from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button

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
    toggle_key : Union[Key, KeyCode]
        Keyboard shortcut to start or stop the auto-clicker.
    stop_key : Union[Key, KeyCode]
        Keyboard shortcut to trigger application shutdown.
    click_button : Button
        The mouse button used for clicking (e.g., Button.left or Button.right).
    click_interval : float
        Delay in seconds between mouse clicks.
    """

    # Applicaion State
    operating: bool = False
    exiting: bool = False

    # Configuration
    toggle_key: Key | KeyCode = Key.f6 # Hotkey to start/stop the auto-clicker (default = F6)
    exit_key: Key | KeyCode = Key.f8 # Hotkey to exit the program (default = F8)
    click_button: Button = Button.right # Mouse button to click (default = right)
    click_interval: float = 10 # Time in seconds between clicks

    @staticmethod
    def key_to_str(key: Key | KeyCode) -> str:
        """
        Converts a key or key code into a human-readable uppercase string.

        Parameters
        ----------
        key : Union[Key, KeyCode]
            The key or key code to convert.

        Returns
        -------
        str
            Readable representation such as "F6" or "A".
        """

        if isinstance(key, Key):
            return key.name.upper()     # Key.f6 → F6
        elif isinstance(key, KeyCode) and key.char:
            return key.char.upper()     # KeyCode('a') → A
        return str(key)

    @property
    def toggle_key_str(self) -> str:
        """
        Returns the string representation of the toggle key.

        Returns
        -------
        str
            Readable hotkey name (e.g., "F6").
        """
        return self.key_to_str(self.toggle_key)

    @property
    def exit_key_str(self) -> str:
        """
        Returns the string representation of the stop key.

        Returns
        -------
        str
            Readable hotkey name (e.g., "F8").
        """
        return self.key_to_str(self.exit_key)
