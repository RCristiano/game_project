from pygame import Rect

class Scene:
    def __init__(self, name: str, game, rect: Rect = None):
        self.name = name
        self.game = game
        self.rect = rect
        self.clickable = False
        self.click = False
        self.entities = []
        self.logger = game.logger
        self.logger.info(f"Scene {self.name} created")

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self):
        if self.clickable and self.rect and (pos := self.game.click(self)):
            if self.rect.collidepoint(pos):
                self.click = True
                self.logger.info(f"Scene {self.name} clicked")
        for entity in self.entities:
            entity.update()