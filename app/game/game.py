import logging
import pygame
from config.config import Config
from scene.scene import Scene


class logger(logging.Logger):
    def __init__(self):
        super().__init__("Game")
        self.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.handler.setFormatter(self.formatter)
        self.addHandler(self.handler)

class Game:
    """ Game Class """
    
    def __init__(self, config: Config):
        self.config = config
        pygame.init()
        pygame.display.set_caption(self.config.TITLE)
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
            self.clock.tick(self.config.FPS)
            self.scene.update(self.clock.get_time())
            self.events()
            pygame.display.flip()
            
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                return event.key
            
    def key_pressed(self, key):
        return pygame.key.get_pressed()[key]