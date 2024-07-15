"""
This module defines the start scene of the game.
"""

from pygame import Surface
from pygame.event import Event
from pygame.font import Font, get_default_font
from pygame.locals import KEYDOWN

from engine.scene import Scene
from engine.logger import logger

from .config import config_scene

start_scene = Scene("Start Screen")


@start_scene.draw("background")
def background(scene: Scene) -> None:
    """
    Draws the background of the start scene.

    Args:
        scene (Scene): The current scene.
    """
    bg_surface = Surface(scene.game.screen.get_size())
    bg_surface.fill((120, 0, 0))
    scene.game.screen.blit(bg_surface, (0, 0))


@start_scene.draw("message")
def message(scene: Scene) -> None:
    """
    Draws the message on the start scene.

    Args:
        scene (Scene): The current scene.
    """
    font = Font(get_default_font(), 80)
    msg = font.render("Press any button", True, (255, 255, 255))
    message_center = msg.get_rect(
        center=(scene.game.config.width / 2, scene.game.config.height / 2)
    )
    scene.game.screen.blit(msg, message_center)


@start_scene.event_listener
def press_any_button(scene: Scene, event: Event) -> None:
    """
    Event listener for the start scene.

    Args:
        scene (Scene): The current scene.
        event (Event): The event triggered.
    """
    if event.type == KEYDOWN:
        logger.info("Button pressed")
        scene.game.scene = config_scene
