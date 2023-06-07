import pygame
from typing import Callable
from pygame import Rect, mouse
from pygame.constants import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN
from logging import Logger

from protocols.game import Game
from protocols.scene import Scene


class Scene:
    def __init__(
        self, name: str,
        game: Game,
        rect: Rect = Rect(0, 0, 0, 0),
        clickable: bool = False
    ) -> None:
        self.name: str = name
        self.game: Game = game
        self.rect: Rect = rect
        self.clickable: bool = clickable
        self.clicked: bool = False
        self.entities: list[Scene] = []
        self.systems: dict[Callable, tuple] = {}
        self.actions: list[Callable] = []
        self.logger: Logger = game.logger
        self.logger.info(f"Scene {self.name} created")
        
    def add_entity(self, entity: Scene) -> None:
        self.entities.append(entity)
        self.logger.info(f"Entity {entity.name} added to scene {self.name}")
 
    def add_system(self, system: Callable, *args, **kwargs) -> None:
        self.systems[system] = (args, kwargs)
        self.logger.info(f"System {system.__name__} added to scene {self.name}")

    def add_action(self, action: Callable) -> None:
        self.actions.append(action)
        self.logger.info(f"Action {action.__name__} added to scene {self.name}")

    def update(self) -> None:
        for event in pygame.event.get():
            if (event.type == QUIT or ( event.type == KEYDOWN and event.key == K_ESCAPE)):
                self.game.quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.clickable and self.rect.collidepoint(mouse.get_pos()):
                        self.clicked = True
                        self.logger.info(f"Scene {self.name} clicked")
                for entity in self.entities:
                    if entity.clickable and entity.rect.collidepoint(mouse.get_pos()):
                        entity.clicked = True
                        self.logger.info(f"Entity {entity.name} clicked")
            for action in self.actions:
                action(self, event)
        for system in self.systems:
            system(*self.systems[system][0], **self.systems[system][1])
        for entity in self.entities:
            entity.update()