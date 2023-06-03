from pygame import Surface, Rect
from pygame.font import Font, get_default_font
from game.game import Game
from scene.scene import Scene
from scenes.game import GameScene
from scenes.game_over import GameOverScene


class ConfigScene(Scene):

    def __init__(self, game: Game):
        super().__init__("Config Screen", game)
        self.screen = game.screen
        self.config = game.config
        self.rect = self.screen.get_rect()
        self.background = Surface(self.screen.get_size())
        self.font_size = 80
        self.font = Font(get_default_font(), self.font_size)
        self.options = {'New Game': GameScene, 'Quit Game': GameOverScene}
        self.buttons = []
            
    def update(self):
        super().update()
        self.background.fill((0, 120, 0))
        self.screen.blit(self.background, (0, 0))
        x, y = (self.config.WIDTH / 2, self.config.HEIGHT / 2)
        for message in self.options:
            msg = self.font.render(message, 'True', (255, 255, 255))
            msg_pos = msg.get_rect(center=(x, y))
            self.buttons.append(self.screen.blit(msg, msg_pos))
            y += self.font_size + 5