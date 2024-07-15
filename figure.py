import pygame

class Figure():
    def __init__(self, player, type, image):

        self.player = player # 0 - белые, 1 - чёрные
        self.type = type # Тип фигуры
        self.image = image # Изображение фигуры
        self.active = False # Выбрана ли фигура

    def draw(self, screen, x, y, width):
        self.surf_figure = pygame.image.load(self.image)
        self.surf_figure = pygame.transform.scale(self.surf_figure, (width, width))
        self.rect_figure = self.surf_figure.get_rect(topleft=(x * width, y * width))
        screen.blit(self.surf_figure, self.rect_figure)
        if self.active == True:
            pygame.draw.rect(screen, (50, 205, 50), (x * width, y * width, width, width), width=3)

    def check_action(self, field, base_x, base_y):
        for i in range(0, 2):
            for x in range(1, 1 + abs(len(field) ** i - (base_x + 1))):
                if field[base_x - x * (-1) ** i][base_y].figure != None:
                    field[base_x - x * (-1) ** i][base_y].active = True
                    break
                else:
                    field[base_x - x * (-1) ** i][base_y].active = True
            for y in range(1, 1 + abs(len(field[0]) ** i - (base_y + 1))):
                if field[base_x][base_y - y * (-1) ** i].figure != None:
                    field[base_x][base_y - y * (-1) ** i].active = True
                    break
                else:
                    field[base_x][base_y - y * (-1) ** i].active = True


    def pesh_act(self, field, x_base, y_base):
        action_list = []

        for i in range(1, 3):
            y_field = y_base - i * (- 1) ** self.player
            if y_field == 8 or y_field == -1 or field[x_base][y_field].figure != None:
                break
            else:
                action_list.append([x_base, y_field])
        return action_list


