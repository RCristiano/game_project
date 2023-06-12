from pygame import Surface, event
from pygame.font import Font, get_default_font
from pygame.locals import KEYDOWN

from scene.scene import Scene
from scenes.config import ConfigScene


class StartScene(Scene):
    
    def __init__(self, game):
        super().__init__("Start Screen", game)
        background = Surface(game.screen.get_size())
        font = Font(get_default_font(), 80)
        background.fill((120, 0, 0))
        game.screen.blit(background, (0, 0))
        message = font.render("Press any buttom", 'True', (255, 255, 255))
        message_center = message.get_rect(
            center=(game.config.WIDTH / 2, game.config.HEIGHT / 2)
        )
        game.screen.blit(message, message_center)
        def press_any_buttom(scene: Scene, event: event) -> None:
            if event.type == KEYDOWN:
                scene.logger.info("Buttom pressed")
                scene.game.scene = ConfigScene(game)
        self.add_action(press_any_buttom)