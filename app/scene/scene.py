class Scene:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.entities = []
        self.systems = []
        self.logger = game.logger
        self.logger.info(f"Scene {self.name} created")

    def add_entity(self, entity):
        self.entities.append(entity)

    def add_system(self, system):
        self.systems.append(system)

    def update(self, delta_time):
        for system in self.systems:
            system.update(delta_time)