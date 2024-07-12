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
    bg_surface = Surface(scene.game.screen.get_size())
    bg_surface.fill((120, 0, 0))
    scene.game.screen.blit(bg_surface, (0, 0))


@start_scene.draw("message")
def message(scene: Scene) -> None:
    font = Font(get_default_font(), 80)
    message = font.render("Press any buttom", True, (255, 255, 255))
    message_center = message.get_rect(
        center=(scene.game.config.WIDTH / 2, scene.game.config.HEIGHT / 2)
    )
    scene.game.screen.blit(message, message_center)


@start_scene.event_listener
def press_any_buttom(scene: Scene, event: Event) -> None:
    if event.type == KEYDOWN:
        logger.info("Buttom pressed")
        # scene.game.scene = config_scene
