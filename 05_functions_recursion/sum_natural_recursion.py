# Sum of first n natural numbers using recursion

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

num = int(input("Enter n: "))
print(f"Sum of first {num} natural numbers = {sum_n(num)}")
