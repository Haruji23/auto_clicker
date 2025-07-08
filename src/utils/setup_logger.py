"""
Logger setup utility with rich console output and file handlers.

Functions:
    setup_logger(debug_mode, log_dir): Initialize logger with color console and split log files.

Args:
    debug_mode (bool): Whether to enable DEBUG level in console.
    log_dir (str): Directory to store log files.
"""

from rich.console import Console
from rich.logging import RichHandler
import logging
from pathlib import Path


def setup_logger(debug_mode: bool = False, log_dir: str = "logs") -> None:
    """
    Setup logger with:
    - Rich console output (styled like cyber terminal)
    - File output (debug/info/error) split by level
    - Uses green/teal theme with glitch emoji

    Args:
        debug_mode (bool): Show DEBUG logs in console if True
        log_dir (str): Directory to store log files
    """
    # === Base logger setup ===
    logging.basicConfig(handlers=[], force=True)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    Path(log_dir).mkdir(parents=True, exist_ok=True)

    # === Rich Console Handler ===
    console_handler = RichHandler(
        rich_tracebacks=True,
        markup=True,
        log_time_format="[%H:%M:%S]",
        show_level=True,
        show_path=False
    )
    console_handler.setLevel(logging.DEBUG if debug_mode else logging.INFO)
    logger.addHandler(console_handler)

    # === Format for file logs ===
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    if debug_mode:
        # === DEBUG only → logs/debug.log ===
        debug_file = logging.FileHandler(f"{log_dir}/debug.log", mode="w", encoding="utf-8")
        debug_file.setLevel(logging.DEBUG)
        debug_file.addFilter(lambda r: r.levelno == logging.DEBUG)
        debug_file.setFormatter(formatter)
        logger.addHandler(debug_file)

    # === INFO only → logs/info.log ===
    info_file = logging.FileHandler(f"{log_dir}/info.log", mode="w", encoding="utf-8")
    info_file.setLevel(logging.INFO)
    info_file.addFilter(lambda r: r.levelno == logging.INFO)
    info_file.setFormatter(formatter)
    logger.addHandler(info_file)

    # === WARNING+ → logs/error.log ===
    err_file = logging.FileHandler(f"{log_dir}/error.log", mode="w", encoding="utf-8")
    err_file.setLevel(logging.WARNING)
    err_file.setFormatter(formatter)
    logger.addHandler(err_file)

    # Summary log
    logger.info("[bold cyan]🚀 Logger initialized. Debug mode: %s[/]", debug_mode)
