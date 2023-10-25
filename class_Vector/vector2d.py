"""
vector2d.py: упращенный класс, демонстрирующий некоторые специальные методы.

Сложение::
    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

Абсолютная величина::
    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0

Умножение на скаляр:
    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0

"""

import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def return_self(self):
        return self

    def __bool__(self):
        return bool(abs(self))


    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v = Vector(0, 0)

print(v.return_self())

