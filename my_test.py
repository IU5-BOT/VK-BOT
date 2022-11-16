# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>

class Line:
    def __init__(self, x: int, y: int, cost: int, both):
        self._x: int = x
        self._y: int = y
        self._cost: int = cost
        self._both: bool = both

    def __str__(self):
        return f'{self._x}, {self._y}, {self._cost}, {self._both}'

    @property
    def x(self):
        return self._x

    @property
    def cost(self):
        return self._cost

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y


def get_line(start_point, line: list) -> list:
    return [el for el in line if el.x == start_point]


POINTS = [
    (1, 2),
    (3, 4),
    (5, 6),
    (7, 8),
]
LINES = []
# Для С++.
for i in range(6):
    a, b, s = int(input('a=')), int(input('b=')), 5
    flag_res: bool = False
    # Проверка, есть ли уже такая
    for el in LINES:
        if (el.x == a or el.x == b) and (el.y == b or el.y == a):
            flag_res = True
            break
    LINES.append(Line(a, b, s, flag_res))
# Печать результата ввода.
for el in LINES:
    print(el)

# Поиск пути.
start, end = int(input('a=')), int(input('b='))
best_sum = 0
best_way = None
for line in LINES:
    res_sum = 0
    if start == line.x and line.cost > best_sum:
        best_sum += line.cost
        best_way = line.y
