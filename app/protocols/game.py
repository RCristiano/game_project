from logging import Logger
from typing import Protocol
from pygame import Surface
from pygame.time import Clock

from protocols.config import Config


class Game(Protocol):
    config: Config
    init: tuple[int, int]
    clock: Clock
    screen: Surface
    running: bool
    scene: 'Scene'
    logger: Logger

    def run(self, start_scene: 'Scene'):
        """ Game Loop """
    
    def quit(self):
        """ Quit Game """