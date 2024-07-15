import pygame

class Tile():
    def __init__(self, color, figure = None):
        self.color = color
        self.figure = figure
        self.active = False
        self.surf = None
        self.rect = None


    def draw(self, screen, x, y, width):
        pygame.draw.rect(screen, self.color, (x * width, y * width, width, width))
        self.surf = pygame.Surface((width, width))
        self.rect = self.surf.get_rect(topleft=(x * width, y * width))
        if self.figure != None:
            self.figure.draw(screen, x, y, width)
        if self.active == True:
            pygame.draw.rect(screen, (50, 205, 50), (x * width, y * width, width, width), width = 3)
