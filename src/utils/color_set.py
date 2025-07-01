from logging import INFO, Formatter, ERROR, DEBUG, WARNING, CRITICAL
from config.constants import WHITE, CYAN, YELLOW, RED, DARK_RED

# color func
cyan = lambda x: f"\033[36m{x}\033[0m"
yellow = lambda x: f"\033[33m{x}\033[0m"
bold = lambda x: f"\033[1m{x}\033[0m"
green = lambda x: f"\033[32m{x}\033[0m"
red = lambda x: f"\033[31m{x}\033[0m"

class ColorFormatter(Formatter):
    COLORS = {
        DEBUG:    WHITE,  # white
        INFO:     CYAN,  # blue
        WARNING:  YELLOW,  # yellow
        ERROR:    RED,  # red
        CRITICAL: DARK_RED,  # dark red
    }
    RESET = "\033[0m"

    def format(self, record):
        msg = super().format(record)
        if "[green]" in msg:
            return f"\033[32m{msg.replace('[green]', '')}\033[0m"
        elif "[red]" in msg:
            return f"\033[31m{msg.replace('[red]', '')}\033[0m"
        color = self.COLORS.get(record.levelno, self.RESET)
        message = super().format(record)
        return f"{color}{message}{self.RESET}"