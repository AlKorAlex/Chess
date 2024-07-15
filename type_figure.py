from abc import ABC, abstractmethod
import pygame

class Type(ABC):
    @abstractmethod
    def check_action(self, player, field, base_x, base_y):
        pass

class Peshka(Type):
    def __init__(self):
        self.image = ['image/Пешка Белая.png', 'image/Пешка Чёрная.png']

    def check_action(self, player, field, base_x, base_y):
        if base_y != (-5 * (player - 1) + 1):
            turn = 2
        else:
            turn = 3
        for i in range(1, turn):
            field_y = base_y - i * (- 1) ** player
            if field_y == 8 or field_y == -1 or field[base_x][field_y].figure != None:
                break
            else:
                field[base_x][field_y].active = True
        for i in range(0, 2):
            y = base_y - (- 1) ** player
            x = base_x - (- 1) ** i
            if x > 7 or x < 0 or y > 7 or y < 0:
                break
            elif field[x][y].figure != None and field[x][y].figure.player != player:
                field[x][y].active = True

class Ladya(Type):
    def __init__(self):
        self.image = ['image/Ладья Белая.png', 'image/Ладья Чёрная.png']

    def check_action(self, player, field, base_x, base_y):
        for i in range(0, 2):
            for x in range(1, 1 + abs(len(field) ** i - (base_x + 1))):
                if field[base_x - x * (-1) ** i][base_y].figure != None:
                        if field[base_x - x * (-1) ** i][base_y].figure.player != player:
                            field[base_x - x * (-1) ** i][base_y].active = True
                            break
                        else:
                            break
                else:
                    field[base_x - x * (-1) ** i][base_y].active = True
            for y in range(1, 1 + abs(len(field[0]) ** i - (base_y + 1))):
                if field[base_x][base_y - y * (-1) ** i].figure != None:
                    if field[base_x][base_y - y * (-1) ** i].figure.player != player:
                        field[base_x][base_y - y * (-1) ** i].active = True
                        break
                    else:
                        break
                else:
                    field[base_x][base_y - y * (-1) ** i].active = True

class King(Type):
    def __init__(self):
        self.image = ['image/Король Белый.png', 'image/Король Чёрный.png']

    def check_action(self, player, field, base_x, base_y):
        for y in range (base_y - 1, base_y + 2):
            if y > 7 or y < 0:
                continue
            if y == base_y:
                step = 2
            else:
                step = 1
            for x in range(base_x - 1, base_x + 2, step):
                if x > 7 or x < 0:
                    continue
                if field[x][y].figure != None and field[x][y].figure.player == player:
                    continue
                else:
                    field[x][y].active = True

class Slon(Type):
    def __init__(self):
        self.image = ['image/Слон Белый.png', 'image/Слон Чёрный.png']

    def check_action(self, player, field, base_x, base_y):
        x_t = -1
        y_t = -1

        for i in range(0, 4):
            for j in range(1, 8):
                check_x = base_x + j * (x_t)
                check_y = base_y + j * (y_t)
                if check_x < 0 or check_y < 0 or check_x > 7 or check_y > 7:
                    break
                else:
                    print('i = ', i, '  j = ', j, '  x = ', check_x, '  y = ', check_y)
                    tile = field[check_x][check_y]
                    if tile.figure != None:
                        if tile.figure.player != player:
                            tile.active = True
                            break
                        else:
                            break
                    else:
                        tile.active = True
            y_t = -y_t
            if i == 1:
                x_t = 1

class Ferz(Type):
    def __init__(self):
        self.image = ['image/Ферзь Белый.png', 'image/Ферзь Чёрный.png']

    def check_action(self, player, field, base_x, base_y):
        x_t = -1
        y_t = -1

        for i in range(0, 4):
            for j in range(1, 8):
                check_x = base_x + j * (x_t)
                check_y = base_y + j * (y_t)
                if check_x < 0 or check_y < 0 or check_x > 7 or check_y > 7:
                    break
                else:
                    tile = field[check_x][check_y]
                    if tile.figure != None:
                        if tile.figure.player != player:
                            tile.active = True
                            break
                        else:
                            break
                    else:
                        tile.active = True
            y_t = -y_t
            if i == 1:
                x_t = 1


        for i in range(0, 2):
            for x in range(1, 1 + abs(len(field) ** i - (base_x + 1))):
                if field[base_x - x * (-1) ** i][base_y].figure != None:
                    if field[base_x - x * (-1) ** i][base_y].figure.player != player:
                        field[base_x - x * (-1) ** i][base_y].active = True
                        break
                    else:
                        break
                else:
                    field[base_x - x * (-1) ** i][base_y].active = True
            for y in range(1, 1 + abs(len(field[0]) ** i - (base_y + 1))):
                if field[base_x][base_y - y * (-1) ** i].figure != None:
                    if field[base_x][base_y - y * (-1) ** i].figure.player != player:
                        field[base_x][base_y - y * (-1) ** i].active = True
                        break
                    else:
                        break
                else:
                    field[base_x][base_y - y * (-1) ** i].active = True

class Horse(Type):
    def __init__(self):
        self.image = ['image/Конь Белый.png', 'image/Конь Чёрный.png']

    def check_action(self, player, field, base_x, base_y):
        for k in range(0, 2):
            for i in range(0, 2):
                for j in range(0, 2):
                    check_x = base_x + (- 1) ** i + (- 1) ** i * 0 ** k
                    check_y = base_y + (- 1) ** j + (- 1) ** j * 0 ** 0 ** k
                    if check_x < 0 or check_y < 0 or check_x > 7 or check_y > 7:
                        continue
                    else:
                        tile = field[check_x][check_y]
                        if tile.figure != None:
                            if tile.figure.player != player:
                                tile.active = True
                                continue
                            else:
                                continue
                        else:
                            tile.active = True


class Figure():
    def __init__(self, player, type):
        self.player = player
        self.active = False
        match type:
            case 'Пешка':
                self.type = Peshka()
            case 'Ладья':
                self.type = Ladya()
            case 'Конь':
                self.type = Horse()
            case 'Ферзь':
                self.type = Ferz()
            case 'Король':
                self.type = King()
            case 'Слон':
                self.type = Slon()

    def draw(self, screen, x, y, width):
        self.surf_figure = pygame.image.load(self.type.image[self.player])
        self.surf_figure = pygame.transform.scale(self.surf_figure, (width, width))
        self.rect_figure = self.surf_figure.get_rect(topleft=(x * width, y * width))
        screen.blit(self.surf_figure, self.rect_figure)
        if self.active == True:
            pygame.draw.rect(screen, (50, 205, 50), (x * width, y * width, width, width), width=3)

    def check_action(self, field, base_x, base_y):
        self.type.check_action(self.player, field, base_x, base_y)






