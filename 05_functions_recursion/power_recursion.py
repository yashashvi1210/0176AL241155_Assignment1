# Power of a number (x^n) using recursion

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    return x * power(x, n - 1)

x = float(input("Enter base (x): "))
n = int(input("Enter exponent (n): "))
print(f"{x} ^ {n} = {power(x, n)}")
