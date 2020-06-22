from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, self1):
        d = sqrt((self.x - self1.x) ** 2 + (self.y - self1.y) ** 2)
        return f'{d:.{1}f}'


# p1 = Point(1.5, 1)
# p2 = Point(1.2, 5)
# print(p1.dist(p2))
