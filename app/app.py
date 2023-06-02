from game.game import Game
from config.config import Config
from scenes.start import StartScene


if __name__ == "__main__":
    config = Config()
    game = Game(config)
    game.run(StartScene)