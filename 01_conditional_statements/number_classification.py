# Number Classification

num = int(input("Enter a number: "))

# Positive / Negative / Zero
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Even / Odd
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Divisible by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")
