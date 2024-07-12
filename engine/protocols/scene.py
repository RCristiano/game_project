"""
This module defines the ProtoScene protocol, which represents a prototype scene in the game engine.
"""

from typing import Callable, Protocol, Self

import pygame

from engine.protocols.entity import Entity


class ProtoScene(Protocol):
    """
    Represents a prototype scene in the game engine.

    Attributes:
        name (str): The name of the scene.
        entities (set[Self]): The set of entities in the scene.
        systems (dict[Callable, tuple]): The dictionary of systems and their arguments.
        actions (set[Callable]): The set of actions in the scene.
        drawings (set[Callable]): The set of drawings in the scene.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ProtoScene class.

        Args:
            name (str): The name of the scene.
        """
        ...

    def draw(self) -> None:
        """
        Draws the scene.
        """
        ...

    def add_entity(self, entity: Entity) -> None:
        """
        Adds an entity to the scene.

        Args:
            entity (Entity): The entity to add.
        """
        ...

    def add_system(self, system: Callable, *args, **kwargs) -> None:
        """
        Adds a system to the scene.

        Args:
            system (Callable): The system to add.
            *args: Variable length argument list for the system.
            **kwargs: Arbitrary keyword arguments for the system.
        """
        ...

    def action(self, action: Callable) -> None:
        """
        Adds an action to the scene.

        Args:
            action (Callable): The action to add.
        """
        ...

    def update(self, game, event: pygame.event.Event | None = None) -> None:
        """
        Updates the scene.

        Args:
            game: The game object.
            event (pygame.event.Event | None): The event object, if any.
        """
        ...
