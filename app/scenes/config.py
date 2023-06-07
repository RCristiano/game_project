from pygame import Surface, Rect
from pygame.font import Font, get_default_font

from protocols.game import Game
from protocols.config import Config
from scene.scene import Scene
from scenes.game import GameScene
from scenes.game_over import GameOverScene


class ConfigScene(Scene):

    def __init__(self, game: Game):
        super().__init__("Config", game)
        self.screen: Surface = game.screen
        self.config: Config = game.config
        self.rect: Rect = self.screen.get_rect()
        self.background = Surface(self.screen.get_size())
        self.font_size = 80
        self.font = Font(get_default_font(), self.font_size)
        self.options = {'New Game': GameScene, 'Quit Game': GameOverScene}
        self.buttons = []
        self.draw_menu()

    def draw_menu(self):
        self.background.fill((0, 120, 0))
        self.screen.blit(self.background, (0, 0))
        x, y = (self.config.WIDTH / 2, self.config.HEIGHT / 2)
        for message in self.options:
            msg = self.font.render(message, 'True', (255, 255, 255))
            msg_pos = msg.get_rect(center=(x, y))
            button_rect = self.screen.blit(msg, msg_pos)
            buttom = Scene(message, self.game, button_rect, True)
            self.add_entity(buttom)
            y += self.font_size + 5