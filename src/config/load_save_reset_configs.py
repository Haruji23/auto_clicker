import json
from logging import exception, warning, error, info, debug
from pathlib import Path
from config.constants import DEFAULT_CONFIGS, CONFIGS_PATH

def load_configs(path: str | None = None) -> dict:
    """
    Loads configuration data from a JSON file.

    If no path is provided, it defaults to CONFIGS_PATH.
    If the file is missing, corrupted, or unreadable, this function will:
    - Log a warning and fallback to DEFAULT_CONFIGS
    - Ensure all required config keys are populated via `check_configs()`
    - Return a complete config dictionary

    Args:
        path (str | None): Optional path to a custom config file. If None, default path is used.

    Returns:
        dict: Validated configuration dictionary ready for use.
    """

    try:
        # Determine which config file to load
        target = Path(path) if path else CONFIGS_PATH
        
        # Attempt to load and validate JSON config
        with open(target, "r") as f:
            config = check_configs(json.load(f))
            debug(f"Loaded_configs: {config}")
            return config
    
    # Handle: file missing
    except FileNotFoundError:
        warning(f"Config file not found: {target}")
        info("Will use the Default Configs instead.")
        return DEFAULT_CONFIGS
    
    # Handle: invalid JSON format
    except json.JSONDecodeError:
        warning(f"Error: Could not decode JSON from {target.name}. Check file format.")
        info("Will use the Default Configs instead.")
        return DEFAULT_CONFIGS
    
    # Handle: any other error during reading/parsing
    except Exception as e:
        exception(f"An unexpected error occurred: {e}")
        info("Will use the Default Configs instead.")
        return DEFAULT_CONFIGS

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
    try:
        
        # Attempt to write config to disk with nice indentation
        with open(CONFIGS_PATH, "w") as f:
            json.dump(config, f, indent=4)
    
    # Handle: cannot write due to permission restrictions
    except PermissionError:
        error("Permission denied: Cannot write to 'current_configs.json'")
    
    # Handle: file path invalid or directory missing
    except FileNotFoundError:
        error("Path not found: Could not create or find 'current_configs.json'")
    
    # Handle: dictionary contains non-serializable data (e.g., Enum, Key, etc.)
    except TypeError as e:
        error(f"Config contains non-serializable data: {e}")
    
    # Handle: general OS-related errors
    except OSError as e:
        exception(f"Unexpected OS error while saving config: {e}")

def check_configs(config: dict) -> dict:
    """
    Validates a configuration dictionary by filling in any missing keys with default values.

    This ensures that the config is always complete and safe to use in downstream logic.

    Args:
        config (dict): The configuration dictionary to validate and complete.

    Returns:
        dict: A full configuration dict with no missing keys.
    """
    if "toggle_key" not in config:
        config["toggle_key"] = DEFAULT_CONFIGS["toggle_key"]
    if "exit_key" not in config:
        config["exit_key"] = DEFAULT_CONFIGS["exit_key"]
    if "button" not in config:
        config["button"] = DEFAULT_CONFIGS["button"]
    if "interval" not in config:
        config["interval"] = DEFAULT_CONFIGS["interval"]
    return config
    

def reset_configs():
    """
    Resets the application configuration to its default values.

    This function immediately overwrites any existing config file 
    with `DEFAULT_CONFIGS`, ensuring that all settings are returned 
    to their original factory defaults. It logs a confirmation message 
    to indicate that the reset was successful.

    Use this method when the user explicitly requests a full reset 
    (e.g., via the `--reset` flag on CLI).
    
    Returns:
        None
    """

    # Overwrite current config file with the hard-coded default values
    save_configs(config=DEFAULT_CONFIGS)

    # Log a confirmation message to indicate success
    info("[green]Configs reset to default.")
    