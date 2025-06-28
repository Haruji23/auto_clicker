from logging import basicConfig, INFO, DEBUG

def setup_logger()-> None:
    """
    Configures global logging behavior for the application.

    This function sets the logging level to INFO and defines a consistent message format
    for all log outputs. The log format includes a timestamp, the log level name, and
    the actual message. This setup helps ensure that logs are easy to read and debug,
    particularly during development or runtime diagnostics.

    Returns
    -------
    None
        This function does not return any value.
    """
    basicConfig(
        level=INFO,
        format='[%(asctime)s] %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )