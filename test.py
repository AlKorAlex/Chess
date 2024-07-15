
class Test():
    def __init__(self):
        self.field = []

        for x in range(0, 8):
            self.field.append([])
            for y in range(0, 8):
                self.field[x].append(0)
        self.base_x = None
        self.base_y = None

    def create_figure(self, x, y):
        self.field[x][y] = 'X'
        self.base_x = x
        self.base_y = y

    def lady(self):
        for i in range(0, 2):
            for x in range(1, 1 + abs(len(self.field) ** i - (self.base_x+1))):
                print(self.base_x - x * (-1)**i)
                self.field[self.base_x - x * (-1)**i][self.base_y] = 'M'
            for y in range(1, 1 + abs(len(self.field[0]) ** i - (self.base_y + 1))):
                print(self.base_y - y * (-1) ** i)
                self.field[self.base_x][self.base_y - y * (-1) ** i] = 'M'

    def draw(self):
        for y in range(0, 8):
            for x in range(0, 8):
                print(self.field[x][y], ' ', end= '')
            print()

test = Test()
test.create_figure(6, 6)
test.lady()
test.draw()