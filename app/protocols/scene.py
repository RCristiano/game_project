from logging import Logger
from typing import Callable, Protocol
from pygame import Rect
from pygame.event import Event

from protocols.game import Game
from protocols.entity import Entity


class Scene(Protocol):
    name: str
    game: Game
    rect: Rect
    clickable: bool
    click: bool
    entities: list[Entity]
    systems: dict[Callable, tuple]
    actions: list[tuple[Event, Callable]]
    logger: Logger

    def update(self):
        """Update the scene"""