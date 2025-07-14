"""
Logger setup utility with rich console output and file handlers.

Functions:
    setup_logger(debug_mode, log_dir): Initialize logger with color console and split log files.

Args:
    debug_mode (bool): Whether to enable DEBUG level in console.
    log_dir (str): Directory to store log files.
"""

from rich.logging import RichHandler
from pathlib import Path
from logging import getLogger, basicConfig, WARNING, DEBUG, INFO, Formatter, FileHandler


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
    # === Rich Console Handler ===
    console_handler = RichHandler(
        rich_tracebacks=True,
        markup=True,
        log_time_format="%H:%M:%S",
        show_level=True,
        show_path=False,
        keywords=[
            "MainThread", 
            "ClickerThread", 
            "KeyboardListenerThread", 
            "ListenerManager", 
            "EventTrace", 
            "EventWarn",
            "Observer",
            "State",
            "Router",
            "Dispatch",
            "Lifecycle",
        ]
    )
    console_handler.setLevel(DEBUG if debug_mode else INFO)
    
    # === Base logger setup ===
    basicConfig(
        handlers=[console_handler], 
        force=True,
        format="%(threadName)s %(message)s",
    )
    logger = getLogger(name="AutoClicker")
    logger.setLevel(DEBUG)

    Path(log_dir).mkdir(parents=True, exist_ok=True)

    # === Format for file logs ===
    file_formatter = Formatter(
        fmt="%(asctime)s [%(threadName)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    if debug_mode:
        # === DEBUG only → logs/debug.log ===
        debug_file = FileHandler(f"{log_dir}/debug.log", mode="w", encoding="utf-8")
        debug_file.setLevel(DEBUG)
        debug_file.addFilter(lambda r: r.levelno == DEBUG)
        debug_file.setFormatter(file_formatter)
        logger.addHandler(debug_file)

    # === INFO only → logs/info.log ===
    info_file = FileHandler(f"{log_dir}/info.log", mode="w", encoding="utf-8")
    info_file.setLevel(INFO)
    info_file.addFilter(lambda r: r.levelno == INFO)
    info_file.setFormatter(file_formatter)
    logger.addHandler(info_file)

    # === WARNING+ → logs/error.log ===
    err_file = FileHandler(f"{log_dir}/error.log", mode="w", encoding="utf-8")
    err_file.setLevel(WARNING)
    err_file.setFormatter(file_formatter)
    logger.addHandler(err_file)

    # Summary log
    logger.info(f"Logger initialized. Debug mode: {debug_mode}")
