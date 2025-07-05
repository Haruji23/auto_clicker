"""
Validate configuration structure and types.

This module checks that a given config dictionary contains all required fields
and valid data types. Intended to be used after loading or before saving configs.

Functions:
    check_configs(config: dict) -> dict: Validate the configuration against expected schema.
"""

from config.constants import DEFAULT_CONFIGS
from logging import error, info, warning
from utils.is_key import is_key
from utils.is_button import is_mouse_button

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
        warning("[bold green]Toggle key[/] [bold red]Not Exist[/]")
        info(f"Set to [bold]{DEFAULT_CONFIGS["toggle_key"]}[/](Default Value)")
        config["toggle_key"] = DEFAULT_CONFIGS["toggle_key"]
    elif not isinstance(config["toggle_key"], str) or not is_key(config["toggle_key"]):
        error("[bold green]Toggle key[/]'s [bold red]Invalid !!![/]")
        info(f"Set to [bold]{DEFAULT_CONFIGS["toggle_key"]}[/](Default Value)")
        config["toggle_key"] = DEFAULT_CONFIGS["toggle_key"]
    
    if "exit_key" not in config:
        warning("[bold magenta]Exit key[/] [bold red]Not Exist[/]")
        info(f"Set to [bold]{DEFAULT_CONFIGS["exit_key"]}[/](Default Value)")
        config["exit_key"] = DEFAULT_CONFIGS["exit_key"]
    elif not isinstance(config["exit_key"], str) or not is_key(config["exit_key"]):
        error("[bold magenta]Exit key[/]'s [bold red]Invalid !!![/]")
        info(f"Set to [bold]{DEFAULT_CONFIGS["exit_key"]}[/](Default Value)")
        config["exit_key"] = DEFAULT_CONFIGS["exit_key"]
    
    if "button" not in config:
        warning("[bold cyan]Click Button[/]'s [bold red]Not Exist[/]")
        info(f"Set to [bold]{DEFAULT_CONFIGS["button"]}[/](Default Value)")
        config["button"] = DEFAULT_CONFIGS["button"]
    elif not isinstance(config["button"], str) or not is_mouse_button(config["button"]):
        error("[bold cyan]Click Button[/]'s [bold red]Invalid !!![/]")
        info(f"Set to [bold]{DEFAULT_CONFIGS["button"]}[/](Default Value)")
        config["button"] = DEFAULT_CONFIGS["button"]

    if "interval" not in config:
        warning("[bold cyan]Click Interval Timer[/]'s [bold red]Not Exist[/]")
        info(f"Set to [bold]{DEFAULT_CONFIGS["interval"]}[/](Default Value)")
        config["interval"] = DEFAULT_CONFIGS["interval"]
    elif not isinstance(config["interval"], float): 
        error("[bold cyan]Click Interval Timer[/]'s [bold red]Invalid !!![/]")
        info(f"Set to [bold]{DEFAULT_CONFIGS["interval"]}[/](Default Value)")
        config["interval"] = DEFAULT_CONFIGS["interval"]

    return config