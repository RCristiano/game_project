import os
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from game.game import Game
from config.config import Config
from scenes.start import StartScene

def quit_game(game) -> None:
    def quit(scene, event):
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            scene.logger.info("Quit game")
            scene.game.quit()
    game.scene.add_action(quit)

if __name__ == "__main__":
    config = Config(os.path.join(os.path.dirname(__file__), 'config/config.ini'))
    game = Game(config)
    game.script = quit_game
    start_scene = StartScene(game)
    game.run(start_scene)