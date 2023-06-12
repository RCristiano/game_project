from logging import Logger
from typing import Callable, Protocol, Self

from protocols.game import Game
from protocols.entity import Entity


class Scene(Protocol):
    name: str
    game: Game
    entities: list[Self]
    systems: dict[Callable, tuple] 
    actions: list[Callable] 
    logger: type[Logger]

    def __init__(self, name: str, game: Game) -> None:
        ...

    def add_entity(self, entity: Entity) -> None:
        ...

    def add_system(self, system: Callable, *args, **kwargs) -> None:
        ...

    def add_action(self, action: Callable) -> None:
        ...

    def update(self) -> None:
        ...