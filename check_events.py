import pygame

class Check_Events():
    def __init__(self, game_stats):
        self.game_stats = game_stats

    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for x in range(0, 8): # Нажатие на клетку поля
                    for y in range(0, 8):
                        button_clicked = self.game_stats.field[x][y].rect.collidepoint(mouse_pos)
                        if button_clicked:
                            print(x, ' - ', y)
                            return [x, y]
                            # return self.game_stats.field[x][y]
    # def check_events(self, move):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             exit()
    #         elif event.type == pygame.MOUSEBUTTONDOWN:
    #             mouse_pos = pygame.mouse.get_pos()
    #             if move == "choose_bk":
    #                 for j in range(0, 2):  # Нажатие на карты в руке у обоих игроков
    #                     for i in range(0, len(self.game_stats.hand_cards[j])):
    #                         button_clicked = self.game_stats.hand_cards[j][i].rect.collidepoint(
    #                             mouse_pos)
    #                         if button_clicked:
    #                             bk = self.game_stats.hand_cards[j][i]
    #                             print(bk.name)
    #                             return bk
    #             elif move == "question":
    #                 for i in range(0, 2): # Кнопки да и нет (Переделать)
    #                     button_clicked = self.game_stats.quest.buttons_rect[i].collidepoint(mouse_pos)
    #                     if button_clicked and i == 0:
    #                         return True
    #                     elif button_clicked and i == 1:
    #                         return False
    #             elif move == "unit":
    #                 for i in range(0, len(self.game_stats.units_window.units)):
    #                     button_clicked = self.game_stats.units_window.units_rect[i].collidepoint(mouse_pos)
    #                     if button_clicked:
    #                         return i
    #                 for i in range(0, 2): # Кнопки подтвердить и сброс
    #                     button_clicked = self.game_stats.units_window.buttons_rect[i].collidepoint(mouse_pos)
    #                     if button_clicked and i == 0:
    #                         return -1
    #                     elif button_clicked and i == 1:
    #                         return -2

