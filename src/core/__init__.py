"""
Core logic for threading, listener, click operations.
"""

from .clicker import AutoClicker
from .start_operation import start_auto_clicker
from .on_press import create_on_press
from .state import State

__all__ = ["AutoClicker", "start_auto_clicker", "create_on_press", "State"]