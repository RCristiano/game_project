from pygame import Surface
from pygame.font import Font
from pygame.locals import *
from game.game import Game
from scene.scene import Scene
from scenes.config import ConfigScene
import pygame

class StartScene(Scene):
    
    def __init__(self, game: Game):
        super().__init__("Start Screen", game)
        self.screen = game.screen
        self.config = game.config
        self.background = Surface((self.config.WIDTH, self.config.HEIGHT))
        self.background.fill((120, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.font = Font('/usr/share/fonts/TTF/FiraCodeNerdFontPropo-Regular.ttf', 80)
        message = self.font.render("Press start", 'True', (255, 255, 255))
        message_center = message.get_rect(center=(self.config.WIDTH / 2, self.config.HEIGHT / 2))
        self.screen.blit(message, message_center)
        
    def update(self, delta_time):
        if self.game.events():
            self.logger.info("Start pressed")
            self.game.scene = ConfigScene(self.game)