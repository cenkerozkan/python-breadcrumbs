import logging


def get_logger(name):
    # ANSI color codes
    COLORS = {
        "DEBUG": "\033[94m",  # Blue
        "INFO": "\033[92m",  # Green
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[1;91m",  # Bold Red
        "RESET": "\033[0m",  # Reset to default
    }

    class ColoredFormatter(logging.Formatter):
        def format(self, record):
            levelname = record.levelname
            if levelname in COLORS:
                record.levelname = f"{COLORS[levelname]}{levelname}{COLORS['RESET']}"
                record.name = (
                    f"\033[95m{record.name}{COLORS['RESET']}"  # Magenta for logger name
                )
                record.filename = (
                    f"\033[96m{record.filename}{COLORS['RESET']}"  # Cyan for filename
                )
                record.msg = (
                    f"{record.msg}{COLORS['RESET']}"  # Ensure message ends with reset
                )
            return super().format(record)

    logger = logging.getLogger(name)

    # Only add handlers if the logger doesn't have any yet
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        formatter = ColoredFormatter(
            "%(levelname)s - %(asctime)s - %(filename)s:%(lineno)d - %(name)s - %(message)s"
        )
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
