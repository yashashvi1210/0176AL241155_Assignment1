# Using the math module

import math

num = 16
print("Square root of 16:", math.sqrt(num))
print("2 to the power 5:", math.pow(2, 5))
print("Factorial of 5:", math.factorial(5))

angle = 30
rad = math.radians(angle)
print(f"sin({angle}°) =", round(math.sin(rad), 4))
print(f"cos({angle}°) =", round(math.cos(rad), 4))
print(f"tan({angle}°) =", round(math.tan(rad), 4))
