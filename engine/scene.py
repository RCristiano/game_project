""" Scene class for the engine """

from typing import Any, Callable
from pygame.event import Event
from engine.logger import logger


class Scene:
    def __init__(self, name: str | None = None) -> None:
        self.name: str | None = name
        self.entities: set[Scene] = set()
        self.systems: dict[Callable, tuple[Any, ...]] = {}
        self.event_listeners: set[Callable[..., None]] = set()
        self.drawings: dict[str, Callable[..., None]] = {}
        self.to_loop: set[Callable[..., None]] = set()
        self.game: Any = None
        logger.info("Scene %s created", self.name)

    def draw(self, name: str | None = None):
        def decorator(drawing: Callable[..., None]):
            self.drawings[(_name := name or drawing.__name__)] = drawing
            logger.info(f"Draw {_name} added to scene {self.name}")
            return drawing

        return decorator

    def erase(self, name: str) -> None:
        if name in self.drawings:
            self.drawings.pop(name)

    def event_listener(self, event_listener: Callable[..., None]):
        self.event_listeners.add(event_listener)
        logger.info(
            "Event listnet %s added to scene %s", event_listener.__name__, self.name
        )

    def call_event(self, event: Event | None = None) -> None:
        for event_listener in self.event_listeners:
            event_listener(scene=self, event=event)

    def add_entity(self, entity: Any) -> None:
        self.entities.add(entity)
        logger.info(f"Entity {entity.name} added to scene {self.name}")

    def add_system(self, system: Callable, *args, **kwargs) -> None:
        self.systems[system] = {"args": args, "kwargs": kwargs, "result": None}
        logger.info(f"System {system.__name__} added to scene {self.name}")

    def loop(self, loop: Callable[..., None]):
        self.to_loop.add(loop)
        logger.info(f"Loop {loop.__name__} added to scene {self.name}")

    def update(self) -> None:
        for entity in self.entities:
            entity.update()
        for system in self.systems:
            self.systems[system]["result"] = system(
                *self.systems[system]["args"], **self.systems[system]["kargs"]
            )
        for drawing in self.drawings.values():
            drawing(self)
