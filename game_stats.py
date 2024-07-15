# from figure import Figure
from type_figure import Figure
from tile import Tile
from check_events import Check_Events

class Game_stats():
    def __init__(self):
        self.active_player = 0 # Активный игрок (0 - белые, 1 - чёрные)
        self.game_end = False

        self.field = [] #Матрица поля
        for x in range(0, 8):
            self.field.append([])
            for y in range(0, 8):
                if (x + y) % 2 == 0:
                    color = (128, 128, 128)
                else:
                    color = (255, 255, 255)
                self.field[x].append(Tile(color))
        self.action_list = None # Список возможных действий фигуры
        self.action_tile = None # Тайл с выбранной фигурой
        self.check_figure = False
        # self.create_one_figure(3, 3) # Создание фигуры для проверки (Потом удалить)
        self.base_field()

    def full_game(self):
        mas = Check_Events(self).check() # Нажатие на клетку поля
        if mas != None:
            tile = self.field[mas[0]][mas[1]]
            if tile.figure is None and tile.active == False:
                self.clear_action()
            elif tile.active == True:
                self.move(self.action_tile, tile)
                self.active_player = not self.active_player
                print(self.active_player)
            elif tile.figure != None and tile.figure.player == self.active_player:
                self.clear_action()
                self.action_tile = tile #[mas[0], mas[1]]
                self.check_action(mas[0], mas[1], tile.figure)
                self.action_tile = tile
                tile.figure.active = True


    def create_one_figure(self, player, x, y, type):
        # self.field[x][y].figure = Figure(1, 'Конь')
        self.field[x][y].figure = Figure(player, type)

    def base_field(self): # Базовая расстановка фигур

        for i in range(0, 2): # Пешки
            y = 6 - 5 * i
            for x in range(0, 8):
                # self.field[x][y].figure = Figure(i, 'Пешка')
                self.create_one_figure(i, x, y, 'Пешка')
        fig_mas = ['Ладья', 'Конь', 'Слон']
        for i in range(0, 2):
            for x in range(0, 3):
                for j in range(0, 2):
                    y = 7 - 7 * i
                    self.create_one_figure(i, 7 - x * 0 ** j - (7 - x) * j, y, fig_mas[x])

        fig_mas = ['Король', 'Ферзь']
        for i in range(0, 2):
            y = 7 - 7 * i
            for x in range(3, 5):
                self.create_one_figure(i, x, y, fig_mas[x-3])


    def move(self, tile_base, tile_new):
        self.clear_action()
        tile_new.figure = tile_base.figure
        tile_base.figure = None


    def clear_action(self):
        for x in range(0, 8):
            for y in range(0, 8):
                self.field[x][y].active = False
                if self.action_tile != None:
                    self.action_tile.figure.active = False
                    self.action_tile = None


    def check_action(self, base_x, base_y, figure): # Установка активных тайлов
        self.clear_action()
        figure.check_action(self.field, base_x, base_y)
        # for i in range(0, len(self.action_list)): # Установка обводки для тайлов
        #     y = self.action_list[i][1]
        #     x = self.action_list[i][0]
        #     self.field[x][y].action = True

    def print(self):
        for y in range(0, 8):
            for x in range(0, 8):
                print(self.field[x][y].active, ' ', end='')
            print()

