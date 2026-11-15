# LCM and HCF using loops (no built-in math functions)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# HCF: keep replacing (a, b) with (b, a % b) until b becomes 0
x, y = a, b
while y != 0:
    x, y = y, x % y
hcf = x

# LCM: (a * b) / HCF
lcm = (a * b) // hcf

print("HCF =", hcf)
print("LCM =", lcm)
