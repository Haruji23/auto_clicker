from pathlib import Path

# Dafault configurations
DEFAULT_CONFIGS = {
    "toggle_key": "f6",
    "exit_key": "f8",
    "button": "right",
    "interval": 60.0
}

# Color constants
WHITE  = "\033[37m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
RED = "\033[31m"
DARK_RED = "\033[41m"
YELLOW = "\033[33m"

# File path of the current configurations
CONFIGS_PATH = Path("../settings/current_configs.json")