"""
Constants used across the config module.

Attributes:
    CONFIGS_PATH (Path): Path to the JSON config file.
    DEFAULT_CONFIGS (dict): Default configuration values.
"""

from pathlib import Path

# Dafault configurations
DEFAULT_CONFIGS = {
    "toggle_key": "f6",
    "exit_key": "f8",
    "button": "right",
    "interval": 60.0
}

# File path of the current configurations
CONFIGS_PATH = Path("../settings/current_configs.json")