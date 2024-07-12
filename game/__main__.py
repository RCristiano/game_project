"""
This module serves as the entry point of the game.
It initializes the game configuration, creates a Game instance,
sets the starting scene, and runs the game.
"""

from engine.game import Game
from engine.config import Config
from game.scenes.start import start_scene


def main():
    """
    Entry point of the game.
    Initializes the game configuration, creates a Game instance,
    sets the starting scene, and runs the game.
    """
    config = Config("game/config.ini")
    game = Game(config)
    game.scene = start_scene
    game.run()


if __name__ == "__main__":
    main()
