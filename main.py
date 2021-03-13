from classes import *


circle = Circle(1, 2, 8)
square = Square(4, 4)
triangle = Triangle(5, 5, 5)
b = [circle, square, triangle]
s = []
for i in b:
    s.append(i.area())
print(s)
