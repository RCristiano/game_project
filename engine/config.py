from configparser import ConfigParser
import os

from engine.logger import logger


class Config:
    """Game Config"""

    def __init__(self, config_file: os.PathLike | str = "config.ini"):
        self.config = ConfigParser()
        if not self.config.read(config_file):
            logger.error(f"Config file not found: {config_file}")

            self.config["game"] = {
                "TITLE": "Game",
                "ICON": "",
            }
            self.config["settings"] = {
                "WIDTH": "800",
                "HEIGHT": "600",
                "FPS": "30",
            }
            with open(config_file, "w") as file:
                self.config.write(file)

        self.TITLE = self.config["game"]["TITLE"]
        self.ICON = self.config["game"]["ICON"]
        self.WIDTH = int(self.config["settings"]["WIDTH"])
        self.HEIGHT = int(self.config["settings"]["HEIGHT"])
        self.FPS = float(self.config["settings"]["FPS"])
