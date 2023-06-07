from logging import Logger
from pygame import Surface
from pygame.time import Clock

from protocols.config import Config


class Game:
    config: Config
    init: tuple[int, int]
    clock: Clock
    screen: Surface
    running: bool
    logger: Logger

    def run(self):
        """ Game Loop """