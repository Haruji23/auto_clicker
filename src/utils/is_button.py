from pynput.mouse import Button

def is_mouse_button(button_str: str) -> bool:
    """
    Check if a given string is a recognized mouse button.

    Args:
        button_str (str): The button name (e.g., "left", "right", "middle").

    Returns:
        bool: True if it's a valid mouse button, False otherwise.
    """
    button_str = button_str.lower()
    if hasattr(Button, button_str):
        return True
    return False