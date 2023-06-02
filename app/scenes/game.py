from pygame import Surface
from game.game import Game
from scene.scene import Scene

class GameScene(Scene):
    
    def __init__(self, game: Game):
        super().__init__("Game Screen")
        self.game = game
        self.background = Surface((self.game.config.WIDTH, self.game.config.HEIGHT))
        self.background.fill((120, 0, 0))