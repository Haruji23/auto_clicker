from logging import Handler, LogRecord, Formatter
from textual.widgets import Log

class LogWidgetHandler(Handler):
    def __init__(self, log_widget: Log, formatter: Formatter):
        super().__init__()
        self.log_widget = log_widget
        self.setFormatter(formatter)

    def emit(self, record: LogRecord):
        msg = self.format(record)
        self.log_widget.write(msg)