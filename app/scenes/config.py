import pygame
from pygame import Surface, Rect, draw
from pygame.font import Font, get_default_font

from protocols.game import Game
from scene.scene import Scene


class ConfigScene(Scene):
    
    def __init__(self, game: Game):
        super().__init__("Config", game)
        self.options = {
            'Start': {'selected': True},
            'Configuration': {'selected': False},
            'Quit Game': {'selected': False}
        }
        self.background = Surface(game.screen.get_size())
        self.background.fill((0, 120, 0))
        self.font_size = 80
        self.font = Font(get_default_font(), self.font_size)
        

    def update(self) -> None:
        super().update()
        self.game.screen.blit(self.background, (0, 0))
        x, y = (self.game.config.WIDTH / 2, self.game.config.HEIGHT / 2)
        for option in self.options:
            render = self.font.render(option, 'True', (255, 255, 255))
            position = render.get_rect(center=(x, y))
            rect = self.game.screen.blit(render, position)
            self.options[option]['rect'] = rect
            y += self.font_size + 5
        for option in self.options.values():
            if option['selected']:
                rect = Rect(
                    option['rect'].x - 10,
                    option['rect'].y - 10,
                    option['rect'].width + 20,
                    option['rect'].height + 20
                )
        draw.rect(
            surface=self.game.screen,
            color=(255, 0, 255),
            rect=rect,
            width=5,
            border_radius=10)

# def change_selection(scene: Scene, event: pygame.event) -> None:
#     if event.type == MOUSEBUTTONDOWN and event.button == 1:
#         for option in options.values():
#             if option.rect.collidepoint(pygame.mouse.get_pos()):
#                 for _option in options.values():
#                     _option.selected = False
#                 option.selected = True
#                 index = list(options.values()).index(option)
#                 print(index, option.name)
#     if event.type == KEYDOWN:
#         if event.key == K_DOWN:
#             for option in options.values():
#                 if option.selected:
#                     index = list(options.values()).index(option)
#                     if (index := index + 1) < len(options):
#                         options[list(options)[index]].selected = True
#                         option.selected = False
#         if event.key == K_RETURN:
#             for option in options.values():
#                 if option.selected:
#                     if option.name == 'Start':
#                         scene.game.scene = startScene(scene.game)
#                     if option.name == 'Quit Game':
#                         scene.game.quit()
#     scene.add_action(change_selection)
#     scene.add_system(update)
