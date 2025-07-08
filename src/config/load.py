"""
Load configuration from disk.

This module handles reading the stored configuration file and merging
it with default values if fields are missing. It also gracefully
falls back to defaults if the file is missing or invalid.

Functions:
    load_configs() -> dict: Load and return the current configuration as a dictionary.

Raises:
    OSError: If the file cannot be read.
    json.JSONDecodeError: If the file contains invalid JSON.
    OtherError: If there's the other error
"""


import json
from logging import exception, warning, info, debug
from pathlib import Path
from src.config.constants import DEFAULT_CONFIGS, CONFIGS_PATH
from src.config.validate import check_configs

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