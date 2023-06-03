import logging
import pygame
from pygame.constants import MOUSEBUTTONDOWN
from scene.scene import Scene
from config.config import Config


class logger(logging.Logger):
    def __init__(self):
        super().__init__("Game")
        self.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.handler.setFormatter(self.formatter)
        self.addHandler(self.handler)

class Game:
    """ Game Class """
    
    def __init__(self, config: Config):
        self.config = config
        self.init = pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.config.WIDTH, self.config.HEIGHT))
        self.running = False
        self.scene = None
        self.logger = logger()
        
    def run(self, scene: Scene):
        """ Game Loop """
        self.running = True
        self.scene = scene(self)
        self.logger.info(f"Game started")
        while self.running:
            pygame.display.set_caption(self.config.TITLE)
            self.clock.tick(self.config.FPS)
            self.scene.update()
            for event in pygame.event.get():
                if (
                    event.type == pygame.QUIT
                    or (
                        event.type == pygame.KEYDOWN
                        and event.key == pygame.K_ESCAPE)
                ):
                    self.running = False
                    pygame.quit()
                    quit()
            pygame.display.flip()
            
    def events(self):
        return pygame.event.get()
            
    def key_pressed(self, key):
        return pygame.key.get_pressed()[key]
    
    def mouse_pressed(self):
        return pygame.mouse.get_pressed()
    
    def click(self, scene):
        if scene.clickable:
            for event in self.events():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    return pygame.mouse.get_pos()
        return False