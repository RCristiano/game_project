import pygame
from pygame import Surface, Rect
from pygame.font import Font, get_default_font
from pygame.locals import *

from protocols.game import Game
from scene.scene import Scene


def startScene(game: Game) -> Scene:
    scene = Scene("Start Screen", game)
    background = Surface(game.screen.get_size())
    font = Font(get_default_font(), 80)
    background.fill((120, 0, 0))
    game.screen.blit(background, (0, 0))
    message = font.render("Press start", 'True', (255, 255, 255))
    message_center = message.get_rect(
        center=(game.config.WIDTH / 2, game.config.HEIGHT / 2)
    )
    game.screen.blit(message, message_center)
    def press_any_buttom(scene: Scene, event: pygame.event) -> None:
        if event.type == KEYDOWN:
            scene.logger.info("Buttom pressed")
            scene.game.scene = configScene(scene.game)
    scene.add_action(press_any_buttom)

    return scene

def configScene(game) -> Scene:
    scene = Scene("Config", game)
    options = {'Start': True, 'Configuration': False, 'Quit Game': False}
    background = Surface(game.screen.get_size())
    font_size = 80
    font = Font(get_default_font(), font_size)
    background.fill((0, 120, 0))
    x, y = (game.config.WIDTH / 2, game.config.HEIGHT / 2)
    for message in options:
        msg = font.render(message, 'True', (255, 255, 255))
        msg_pos = msg.get_rect(center=(x, y))
        buttom = Scene(message, game, msg_pos, True)
        buttom.selected = options[message]
        options[message] = buttom
        scene.add_entity(buttom)
        y += font_size + 5
    def update() -> None:
        game.screen.blit(background, (0, 0))
        x, y = (game.config.WIDTH / 2, game.config.HEIGHT / 2)
        for message in options:
            msg = font.render(message, 'True', (255, 255, 255))
            msg_pos = msg.get_rect(center=(x, y))
            game.screen.blit(msg, msg_pos)
            y += font_size + 5
        for option in options.values():
            if option.selected:
                rect = Rect(
                    option.rect.x - 10,
                    option.rect.y - 10,
                    option.rect.width + 20,
                    option.rect.height + 20
                )
        pygame.draw.rect(
            surface=game.screen,
            color=(255, 0, 255),
            rect=rect,
            width=5,
            border_radius=10
        )
    def change_selection(scene: Scene, event: pygame.event) -> None:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            for option in options.values():
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    for _option in options.values():
                        _option.selected = False
                    option.selected = True
                    index = list(options.values()).index(option)
                    print(index, option.name)
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                for option in options.values():
                    if option.selected:
                        index = list(options.values()).index(option)
                        if (index := index + 1) < len(options):
                            options[list(options)[index]].selected = True
                            option.selected = False
            if event.key == K_RETURN:
                for option in options.values():
                    if option.selected:
                        if option.name == 'Start':
                            scene.game.scene = startScene(scene.game)
                        if option.name == 'Quit Game':
                            scene.game.quit()
    scene.add_action(change_selection)
    scene.add_system(update)
    return scene
