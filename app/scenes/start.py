from pygame import Surface
from pygame.font import Font, get_default_font
from pygame.locals import *
from game.game import Game
from scene.scene import Scene
from scenes.config import ConfigScene


class StartScene(Scene):
    
    def __init__(self, game: Game):
        super().__init__("Start Screen", game)
        self.screen = game.screen
        self.config = game.config
        self.background = Surface(self.screen.get_size())
        self.font = Font(get_default_font(), 80)
        
    def update(self):
        super().update()
        self.background.fill((120, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.message = self.font.render("Press start", 'True', (255, 255, 255))
        self.message_center = self.message.get_rect(
            center=(self.config.WIDTH / 2, self.config.HEIGHT / 2)
        )
        self.screen.blit(self.message, self.message_center)
        for event in self.game.events():
            if event.type == KEYDOWN:
                self.logger.info("Start pressed")
                self.game.scene = ConfigScene(self.game)