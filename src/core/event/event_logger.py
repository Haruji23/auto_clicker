from logging import debug, warning, Logger, getLogger

class EventLogger:
    def __init__(self, logger: Logger = getLogger("AutoClicker")):
        self.logger = logger
    def trace(self, msg):
        self.logger.debug(f"[EventTrace] {msg}")

    def warn(self, msg):
        self.logger.warning(f"[EventWarn] {msg}")