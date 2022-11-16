# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>

class Line:
    def __init__(self, x: int, y: int, cost: int, both):
        self._x: int = x
        self._y: int = y
        self._cost: int = cost
        self._both: bool = both
        self._visited = False

    def __str__(self):
        return f'{self._x}, {self._y}, {self._cost}, {self._both}'

    @property
    def x(self):
        return self._x

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, new_visited):
        self._visited = new_visited

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


def get_sum_wait(line, end_point, sum_cost) -> int | None:
    if line.y == end_point:
        return sum_cost

    global TEMP_LINES
    counter_res = 0
    print(line)
    for counter, el in enumerate(TEMP_LINES):
        if el.visited:
            counter_res = counter

        if el.x == line.y and not el.visited:
            el.visited = True
            # try:
            return get_sum_wait(el, end_point, sum_cost + line.cost)
            # except:
            #     print('Не подошла конечная точка')
            #     return None

    old_sum = TEMP_LINES[counter_res].cost
    del TEMP_LINES[counter_res]
    return get_sum_wait(TEMP_LINES[counter_res - 1], end_point, sum_cost - old_sum)


AB = [
    (0, 1),
    (1, 2),
    (2, 4),
    (4, 1),
    (4, 5),
    (5, 3),
    (3, 4),
    (3, 1),
    (0, 5)
]
POINTS = [
    (1, 2),
    (3, 4),
    (5, 6),
    (7, 8),
]
LINES = []
# Для С++.
for i in range(10 - 1):
    # a, b, s = int(input('a=')), int(input('b=')), 5
    a, b, s = AB[i][0], AB[i][1], 1
    flag_res: bool = False
    # Проверка, есть ли уже такая
    for el in LINES:
        if (el.x == a or el.x == b) and (el.y == b or el.y == a):
            flag_res = True
            break
    LINES.append(Line(a, b, s, flag_res))
# Печать результата ввода.
# for el in LINES:
#     print(el)

# Поиск пути.
# start, end = int(input('a=')), int(input('b='))
start, end = 0, 2
TEMP_LINES = LINES[:]
for el in LINES:
    if el.x == start:
        print(get_sum_wait(el, end, 1))
        # global TEMP_LINES
        TEMP_LINES = LINES[:]
        for el2 in LINES:
            el2.visited = True
