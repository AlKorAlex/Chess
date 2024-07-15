import pygame
from settings import Settings
from figure import Figure
from tile import Tile

class Interface():
    def __init__(self, game):
        self.screen = game.screen
        self.field = Field(game.game_stats)


    def draw_line(self):
        self.field.draw(self.screen) # Отрисовка игрового поля


class Field():
    def __init__(self, game_stats = None):
        self.settings = Settings()
        self.game_stats = game_stats

        self.surf = pygame.Surface((self.settings.screen_height, self.settings.screen_height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(topleft=(0, 0))

        self.width = self.settings.screen_height / 8

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        for y in range(0, 8):
            for x in range(0, 8):
                self.game_stats.field[x][y].draw(self.surf, x, y, self.width)

        # for x in range(0, 8):
        #     for y in range(0, 8):
        #         self.game_stats.field[x][y].draw(self.surf, x, y, self.width)
