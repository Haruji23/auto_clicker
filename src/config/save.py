"""
Save configuration data to disk.

This module provides functionality for persisting user configurations
to a JSON file, typically at the end of a `set` command or when updates occur.

Functions:
    save_configs(config: dict) -> None: Save the provided configuration dictionary to disk.

Raises:
    OSError: If the file cannot be written due to IO issues.
    TypeError: If the config object cannot be serialized to JSON.
    PermissionError: If cannot write due to permission restrictions.
    FileNotFoundError: If file path invalid or directory missing.
"""


import json
from logging import exception,error, warning, info
from config.constants import CONFIGS_PATH
from config.validate import check_configs

def save_configs(config: dict) -> None:
    """
    Saves configuration data into the default JSON file path.

    This function ensures all necessary keys exist via `check_configs()` before writing.
    It gracefully handles write-related errors such as permission issues or serialization errors.

    Args:
        config (dict): The configuration dictionary to persist.

    Returns:
        None
    """
    
    # Ensure config contains all required keys
    config = check_configs(config=config)
    
    SETTINGS_DIR = CONFIGS_PATH.parent
    if not SETTINGS_DIR.is_dir():
        SETTINGS_DIR.mkdir(parents=True, exist_ok=True)
        info(f"Created missing directory: {SETTINGS_DIR}")
    
    try:
        
        # Attempt to write config to disk with nice indentation
        with open(CONFIGS_PATH, "w") as f:
            json.dump(config, f, indent=4)
    
    # Handle: cannot write due to permission restrictions
    except PermissionError:
        error(f"Permission denied: Cannot write to {CONFIGS_PATH}")
    
    # Handle: file path invalid or directory missing
    except FileNotFoundError:
        error(f"Path not found: Could not create or find {CONFIGS_PATH}")
    
    # Handle: dictionary contains non-serializable data (e.g., Enum, Key, etc.)
    except TypeError as e:
        error(f"Config contains non-serializable data: {e}")
    
    # Handle: general OS-related errors
    except OSError as e:
        exception(f"Unexpected OS error while saving config: {e}")