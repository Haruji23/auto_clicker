from pynput.keyboard import Key

def is_key(key_str: str) -> bool:
    """
    Check if a given string represents a valid keyboard key.

    Args:
        key_str (str): The key string to validate (e.g., "F6", "space").

    Returns:
        bool: True if the string corresponds to a known key, False otherwise.
    """
    key_str = key_str.lower()
    if hasattr(Key, key_str):
        return True
    elif len(key_str) == 1:
        return True
    return False