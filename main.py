# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
from settings import Settings
from interface import Interface
from game_stats import Game_stats

class Game():
    def __init__(self):
        # Визуальная часть игры
        pygame.init()  # Инициализирует настройки, необходимые Pygame для нормальной работы

        self.settings = Settings()
        # Настройка размера окна и его титульник
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Forbidden Stars - Combat")


        self.FPS = 60  # Частота обновления экрана
        self.clock = pygame.time.Clock()
        self.screen.fill(self.settings.bg_color)

        self.game_stats = Game_stats()
        self.interface = Interface(self)


    def run_game(self):
        """Запуск основного цикла игры"""
        turn = True
        while True:
            # Check_Events(self).check_events(None)
            self.update_screen()
            self.game_stats.full_game()
            turn = False

    def update_screen(self):
        self.interface.draw_line()
        pygame.display.update()
        self.clock.tick(self.FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
