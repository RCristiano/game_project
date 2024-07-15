"""
This module contains the Game class, which represents the main game object.

Attributes:
    _scene (Scene): The current scene of the game.
    config (Config): The configuration object for the game.
    init (tuple): The result of the pygame.init() function.
    clock (Clock): The game clock.
    screen (Surface): The game screen surface.
    running (bool): Flag indicating if the game is running.

Methods:
    __init__(self, config: Config | None = None) -> None:
        Initialize the Game object.

    scene(self) -> Scene:
        Get the current scene.

    scene(self, scene: Scene) -> None:
        Set the current scene.

    run(self) -> None:
        Run the game loop.

    quit(self) -> None:
        Quit the game.
"""

import sys
import pygame
from pygame import Surface
from pygame.time import Clock
from engine.logger import logger
from engine.config import Config
from engine.scene import Scene


class Game:
    """
    The Game class represents the main game object.

    Attributes:
        _scene (Scene): The current scene of the game.
        config (Config): The configuration object for the game.
        init (tuple): The result of the pygame.init() function.
        clock (Clock): The game clock.
        screen (Surface): The game screen surface.
        running (bool): Flag indicating if the game is running.

    Methods:
        __init__: Initialize the Game object.
        scene: Get the current scene.
        scene.setter: Set the current scene.
        run: Run the game loop.
        quit: Quit the game.
    """

    _scene: Scene

    def __init__(self, config: Config | None = None) -> None:
        """
        Initialize the Game object.

        Args:
            config (Config | None): The configuration object for the game.
                Defaults to None.

        Returns:
            None
        """
        self.config: Config = config or Config()
        self.init: tuple = pygame.init()
        self.clock: Clock = pygame.time.Clock()
        self.screen: Surface = pygame.display.set_mode(
            (self.config.width, self.config.height)
        )
        self.running: bool = False
        logger.setLevel(self.config.log_level)

        pygame.display.set_caption(self.config.title)
        if self.config.icon:
            try:
                icon = pygame.image.load(self.config.icon)
                pygame.display.set_icon(icon)
            except FileNotFoundError:
                logger.error("Icon not found: %s", self.config.icon)

    @property
    def scene(self) -> Scene:
        """
        Get the current scene.

        Returns:
            Scene: The current scene.
        """
        return self._scene

    @scene.setter
    def scene(self, scene: Scene) -> None:
        """
        Set the current scene.

        Args:
            scene (Scene): The scene to set.

        Returns:
            None
        """
        self._scene = scene
        self._scene.game = self

    def run(self) -> None:
        """
        Run the game loop.

        Returns:
            None
        """
        self.running = True
        logger.info("Game started")

        while self.running:
            for event in pygame.event.get():
                logger.debug("Event: %s", event)
                if event.type == pygame.QUIT:
                    self.quit()
                self.scene.call_event(event)
            self.scene.update()
            self.clock.tick(self.config.fps)
            pygame.display.flip()
            logger.debug("FPS: %s", self.clock.get_fps())

    def quit(self) -> None:
        """
        Quit the game.

        Returns:
            None
        """
        logger.info("Game stopped")
        self.running = False
        pygame.display.quit()
        pygame.quit()
        sys.exit()

    def show_fps(self) -> None:
        """
        Show the current frames per second on the screen.

        Returns:
            None
        """
        font = pygame.font.Font(None, 36)
        fps = font.render(str(int(self.clock.get_fps())), True, (255, 255, 255))
        self.screen.blit(fps, (10, 10))
