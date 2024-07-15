"""
This module provides a logger configuration for the game engine.

The logger is configured to output log messages to the console with a specific format.
The log level is set to DEBUG, which means all log messages will be displayed.

Usage:
    import logger

    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
"""

import logging


logger = logging.getLogger("Game")
logger.setLevel(logging.NOTSET)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)
