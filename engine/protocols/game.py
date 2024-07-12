from logging import Logger
from typing import Protocol
from pygame import Surface
from pygame.time import Clock

from engine.protocols.config import Config
from engine.protocols.scene import ProtoScene


class ProtoGame(Protocol):
    config: Config
    init: tuple[int, int]
    clock: Clock
    screen: Surface
    running: bool
    scene: ProtoScene

    def run(self):
        """Game Loop"""

    def quit(self):
        """Quit Game"""
