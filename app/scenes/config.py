from pygame import Surface
from pygame.font import Font, get_default_font
from game.game import Game
from scene.scene import Scene

class ConfigScene(Scene):
    
    def __init__(self, game: Game):
        super().__init__("Config Screen", game)
        self.screen = game.screen
        self.config = game.config
        self.background = Surface((self.config.WIDTH, self.config.HEIGHT))
        self.background.fill((0, 120, 0))
        self.screen.blit(self.background, (0, 0))