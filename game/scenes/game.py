from pygame import Surface
from game.game import Game
from scene.scene import Scene

class GameScene(Scene):
    
    def __init__(self, game: Game):
        super().__init__("Game Screen", game)
        self.game = game
        self.background = Surface((self.game.config.WIDTH, self.game.config.HEIGHT))
        self.background.fill((120, 0, 0))
        self.game.screen.blit(self.background, (0, 0))