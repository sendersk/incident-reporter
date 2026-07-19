import logging
import sys


def setup_logger(name: str = "incident-reporter", level: int = logging.INFO) -> logging.Logger:
    """Configures a standardized logger for the application."""

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        logger.addHandler(handler)

    return logger