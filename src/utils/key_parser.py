from pynput.mouse import Button
from pynput.keyboard import Key, KeyCode
from logging import critical, error


def key_mouse_to_str(key: Key | KeyCode | Button) -> str:
    """
    Converts a `Key` or `KeyCode` into a human-readable `uppercase string`.

    Parameters
    ----------
    key : Key | KeyCode
        The key or key code to convert.
    
    Returns
    -------
    string
        Readable representation such as "F6" or "A" or "right".
    """
    try:
        if isinstance(key, Key):
            return key.name.upper()     # Key.f6 → F6
        elif isinstance(key, KeyCode) and key.char:
            return key.char.upper()     # KeyCode('a') → A
        return key.name  # Button.right → right
    except AttributeError as e:
        error(f"{e} Unsupported key type: {key}")
    

def parse_key(key_str: str) -> Key | KeyCode:
    """
    Convert a Readable representation as a key `string` into `Key` or `KeyCode` (f6 -> Key.f6).

    Parameters
    ----------
    key_str : string
        Readable representation of a key (e.g., F6 or f6)
    
    Returns
    -------
    Key | KeyCode
        The classes of representing various keys that may not correspond to letters.
        if it has an error, it will log ValueError
    """
    key_str = key_str.lower()
    try:
        if hasattr(Key, key_str):
            return getattr(Key, key_str)  # such as Key.f6, Key.esc
        elif len(key_str) == 1:
            return KeyCode.from_char(key_str)  # such as 'a', 'b'
    except ValueError:
        critical(f"Unknown key {key_str}")


def parse_button(button_str: str) -> Button:
    """
    Convert the Readable button `string` into `Button` class
    
    Parameters
    ----------
    button_str : string
        Readable button
    
    Returns
    -------
    Button | ValueError
        The various keys. if it has an error, it will log ValueError
    """
    button_str = button_str.lower()
    try:
        if hasattr(Button, button_str):
            return getattr(Button, button_str)
    except ValueError:
        critical(f"Unknown button {button_str}")