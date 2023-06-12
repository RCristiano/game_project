from pygame import event as events
from typing import Any, Callable
from logging import Logger

from game.game import Game
from protocols.scene import Scene


class Scene(Scene):
    def __init__(self, name: str,game: Game) -> None:
        self.name: str = name
        self.game: Game = game
        self.entities: set[Scene] = set()
        self.systems: dict[Callable, tuple[Any, ...]] = {}
        self.actions: set[Callable] = set()
        self.logger: Logger = game.logger(self.name)
        self.logger.info(f"Scene {self.name} created")
        
    def add_entity(self, entity: Scene) -> None:
        self.entities.add(entity)
        self.logger.info(f"Entity {entity.name} added to scene {self.name}")
 
    def add_system(self, system: Callable, *args, **kwargs) -> None:
        self.systems[system] = {'args': args, 'kwargs': kwargs, 'result': None}
        self.logger.info(f"System {system.__name__} added to scene {self.name}")

    def add_action(self, action: Callable[[Any], Any]) -> None:
        self.actions.add(action)
        # self.logger.info(f"Action {action.__name__} added to scene {self.name}")

    def update(self) -> None:
        for event in events.get():
            for action in self.actions:
                action(self, event)
        for system in self.systems:
            self.systems[system]['result'] = system(
                *self.systems[system]['args'],
                **self.systems[system]['kargs'])
        for entity in self.entities:
            entity.update()