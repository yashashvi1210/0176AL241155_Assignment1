# Using our own geometry package (run this file from inside this folder)

from geometry import circle, rectangle

r = 7
print("Circle area:", round(circle.area(r), 2))
print("Circle circumference:", round(circle.circumference(r), 2))

l, w = 10, 5
print("Rectangle area:", rectangle.area(l, w))
print("Rectangle perimeter:", rectangle.perimeter(l, w))
