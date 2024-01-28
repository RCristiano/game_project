import os
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from game.game import Game
from config.config import Config
from scenes.start import StartScene

def script(game) -> None:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            game.quit()

if __name__ == "__main__":
    config = Config(os.path.join(os.path.dirname(__file__), 'config/config.ini'))
    game = Game(config)
    game.script = script
    start_scene = StartScene(game)
    game.run(start_scene)