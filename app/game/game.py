import logging
import pygame
from typing import Any
from pygame import Surface
from pygame.time import Clock

from protocols.scene import Scene
from config.config import Config


class GameLogger(logging.Logger):
    """ Game Logger """

    def __init__(self, name: str = "Game"):
        super().__init__(name)
        self.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.handler.setFormatter(self.formatter)
        self.addHandler(self.handler)

class Game:
    """ Game Class """

    def __init__(self, config: Config):
        self.config: Config = config
        self.init: tuple = pygame.init()
        self.clock: Clock = pygame.time.Clock()
        self.screen: Surface = pygame.display.set_mode((self.config.WIDTH, self.config.HEIGHT))
        self.running: bool = False
        self.scene: Scene = None
        self.script: callable = None
        self.logger: type[logging.Logger] = GameLogger

    def run(self, start_scene: Scene) -> None:
        """ Game Loop"""
        self.running = True
        self.scene = start_scene
        self.logger().info(f"Game started")
        while self.running:
            self.script(self)
            try:
                # icon = pygame.image.load(self.config.ICON)
                # pygame.display.set_icon(icon)
                pygame.display.set_caption(self.config.TITLE)
            except AttributeError as e:
                self.logger().error(e)
                # self.quit()
            self.clock.tick(self.config.FPS)
            self.scene.update() 
            pygame.display.flip()
            
    def quit(self) -> None:
        self.logger().info(f"Game stopped")
        self.running = False
        pygame.quit()
        quit()