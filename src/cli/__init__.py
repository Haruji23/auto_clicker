"""
CLI entrypoint & user-facing display logic.
"""

from .command import command
from .status_display import show_status
from .parse_args import parse_args

__all__ = ["command", "show_status", "parse_args"]