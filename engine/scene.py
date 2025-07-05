"""Scene class for the engine"""

from typing import Any, Callable
from pygame.event import Event
from engine.logger import logger


class Scene:
    """Scene class for the engine"""

    def __init__(self, name: str | None = None) -> None:
        self.name: str | None = name
        self.entities: set[Scene] = set()
        self.systems: dict[Callable[..., Any], tuple[Any, ...]] = {}
        self.event_listeners: set[Callable[..., None]] = set()
        self.drawings: dict[str, Callable[..., None]] = {}
        self.to_loop: set[Callable[..., None]] = set()
        self.game: Any = None
        logger.info("Scene %s created", self.name)

    def draw(self, name: str | None = None):
        """
        Decorator function to add a drawing to the scene.

        Args:
            name (str | None, optional): The name of the drawing.
                If not provided, the name of the decorated function will be
                used. Defaults to None.

        Returns:
            Callable[..., None]: The decorated drawing function.
        """

        def decorator(drawing: Callable[..., None]):
            self.drawings[(_name := name or drawing.__name__)] = drawing
            logger.info("Draw %s added to scene %s", _name, self.name)
            return drawing

        return decorator

    def erase(self, name: str) -> None:
        """
        Removes a drawing from the scene.

        Args:
            name (str): The name of the drawing to be removed.

        Returns:
            None
        """
        if name in self.drawings:
            self.drawings.pop(name)

    def event_listener(self, event_listener: Callable[..., None]):
        """
        Adds an event listener to the scene.

        Parameters:
            event_listener (Callable[..., None]): The event listener function to be added.

        Returns:
            None

        """
        self.event_listeners.add(event_listener)
        logger.info(
            "Event listener %s added to scene %s",
            event_listener.__name__,
            self.name,
        )

    def call_event(self, event: Event | None = None) -> None:
        """
        Notify all registered event listeners by calling them with the current
        scene and the provided event.

        Args:
            event (Event | None): The event to pass to the listeners. Can be None.

        Returns:
            None
        """
        for event_listener in self.event_listeners:
            event_listener(scene=self, event=event)

    def add_entity(self, entity: Any) -> None:
        """
        Add an entity to the scene and log the action.

        Args:
            entity (Any): The entity to add to the scene.

        Returns:
            None
        """
        self.entities.add(entity)
        logger.info("Entity %s added to scene %s", entity.name, self.name)

    def add_system(self, system: Callable, *args, **kwargs) -> None:
        """
        Add a system to the scene with optional arguments and log the action.

        Args:
            system (Callable): The system function to add.
            *args: Positional arguments for the system.
            **kwargs: Keyword arguments for the system.

        Returns:
            None
        """
        self.systems[system] = {"args": args, "kwargs": kwargs, "result": None}
        logger.info("System %s added to scene %s", system.__name__, self.name)

    def loop(self, loop: Callable[..., None]):
        """
        Add a loop function to the scene and log the action.

        Args:
            loop (Callable[..., None]): The loop function to add.

        Returns:
            None
        """
        self.to_loop.add(loop)
        logger.info("Loop %s added to scene %s", loop.__name__, self.name)

    def update(self) -> None:
        """
        Update all entities, run all systems, and execute all drawing functions
        in the scene.

        Returns:
            None
        """
        for entity in self.entities:
            entity.update()
        for system in self.systems:
            self.systems[system]["result"] = system(
                *self.systems[system]["args"], **self.systems[system]["kargs"]
            )
        for drawing in self.drawings.values():
            drawing(self)
