import pygame


class Player:
    """ PyGame Player Class """
    
    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen

    def draw(self):
        """ Draws the player """
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        """ Moves the player """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= 1
        if keys[pygame.K_RIGHT] and self.x < self.screen.get_width():
            self.x += 1
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= 1
        if keys[pygame.K_DOWN] and self.y < self.screen.get_height():
            self.y += 1
        self.draw()