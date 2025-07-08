"""
Reset configuration to default values.

This module overwrites the current config file with the default configuration.
Useful when the user executes a `reset` option in the CLI.

Functions:
    reset_configs() -> None: Restore the configuration file to its default state.

Raises:
    OSError: If the config file cannot be overwritten.
    TypeError: If the config object cannot be serialized to JSON.
    PermissionError: If cannot write due to permission restrictions.
    FileNotFoundError: If file path invalid or directory missing.
"""

from logging import info
from src.config.constants import DEFAULT_CONFIGS
from src.config.save import save_configs


def reset_configs()-> None:
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