# Star patterns: triangle, pyramid, diamond

n = int(input("Enter number of rows: "))

print("\nTriangle:")
for i in range(1, n + 1):
    print("*" * i)

print("\nPyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print("\nDiamond:")
for i in range(1, n + 1):                 # top half
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):             # bottom half
    print(" " * (n - i) + "*" * (2 * i - 1))
