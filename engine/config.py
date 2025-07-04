"""
Module Description

This module contains the Config class which represents the configuration settings for the game.

Author: Your Name
Date: Current Date

"""

from configparser import ConfigParser
import os

from engine.logger import logger


class Config:
    """Game Config

    This class represents the configuration settings for the game.

    Attributes:
        config (ConfigParser): The configuration parser object.
        title (str): The title of the game.
        icon (str): The path to the game's icon.
        width (int): The width of the game window.
        height (int): The height of the game window.
        fps (float): The frames per second of the game.
        show_fps (bool): Flag indicating whether to show the frames per second on the game window.
        log_level (str): The log level for logging.

    Methods:
        __init__: Initializes the Config object and loads the configuration from a file.

    """

    def __init__(self, config_file: os.PathLike[str] | str = "config.ini"):
        self.config = ConfigParser()
        if not self.config.read(config_file):
            logger.error("Config file not found: %s", config_file)

            self.config["game"] = {
                "TITLE": "Game",
                "ICON": "",
            }
            self.config["settings"] = {
                "WIDTH": "800",
                "HEIGHT": "600",
                "FPS": "30",
            }
            with open(config_file, "w", encoding="UTF-8") as file:
                self.config.write(file)

        self.title = self.config.get("game", "TITLE", fallback="Game")
        self.icon = self.config.get("game", "ICON", fallback="")
        self.width = self.config.getint("settings", "WIDTH", fallback=800)
        self.height = self.config.getint("settings", "HEIGHT", fallback=600)
        self.fps = self.config.getfloat("settings", "FPS", fallback=30)
        self.show_fps = self.config.getboolean("debug", "SHOW_FPS", fallback=False)
        self.log_level = self.config.get("debug", "LOG_LEVEL", fallback="NOTSET")
