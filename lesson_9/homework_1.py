"""
1. Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса
Circle (атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра),
Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.

2. Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
"""

import math


class Point:
    def __init__(self, point_x: int, point_y: int):
        self.point_x = point_x
        self.point_y = point_y


class Figure:
    ...


class Circle(Figure):
    def __init__(self, center_point: Point, radius: int):
        self.center_point = center_point
        self.radius = radius

    def get_perimetr(self):
        return round(2 * math.pi * self.radius, 3)

    def get_area(self):
        return round (math.pi * self.radius, 3)


class Triangle(Figure):
    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def get_sides(self):
        side_1 = ((self.point_1.point_x - self.point_2.point_x) ** 2 +
                  (self.point_1.point_y - self.point_2.point_y) ** 2) ** 0.5
        side_2 = ((self.point_2.point_x - self.point_3.point_x) ** 2 +
                  (self.point_2.point_y - self.point_3.point_y) ** 2) ** 0.5
        side_3 = ((self.point_1.point_x - self.point_3.point_x) ** 2 +
                  (self.point_1.point_y - self.point_3.point_y) ** 2) ** 0.5
        return side_1, side_2, side_3

    def get_perimetr(self):
        return round(sum(self.get_sides()), 3)

    def get_area(self):
        half_per = self.get_perimetr() / 2
        s1, s2, s3 = self.get_sides()
        return round((half_per * (half_per - s1) * (half_per - s2) * (half_per - s3)) ** 0.5, 3)


class Square(Figure):
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2

    def get_sides(self):
        side_1 = abs(self.point_1.point_x - self.point_2.point_x)
        side_2 = abs(self.point_1.point_y - self.point_2.point_y)
        return side_1, side_2

    def get_perimetr(self):
        return sum(self.get_sides()) * 2

    def get_area(self):
        s1, s2 = self.get_sides()
        return s1 * s2


if __name__ == "__main__":
    figures = [
        Circle(Point(1, 1), 3),
        Triangle(Point(1, 1), Point(3, 6), Point(1, 9)),
        Square(Point(1, 1), Point(6, 6))
    ]
    for num, figure in enumerate(figures):
        print(f"Figure {num+1} - Area = {figure.get_area()}. Perimetr = {figure.get_perimetr()}")
