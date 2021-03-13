class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Figure):
    def __init__(self, x, y, r):
        self.point = Point(x=x, y=y)
        self.r = r

    def perimeter(self):
        result_p = self.r * (3.14 * 2)
        return result_p

    def area(self):
        result_s = 3.14 * (self.r ** 2)
        return result_s


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        result_p = self.a + self.b + self.c
        return result_p

    def area(self):
        result_s = (self.a + self.b) / 2
        return result_s


class Square(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        result_p = self.a * 2
        return result_p

    def area(self):
        result_s = self.a * 4
        return result_s
