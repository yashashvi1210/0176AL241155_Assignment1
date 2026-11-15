# Using the random module: OTP, random password, random list

import random
import string

# 6-digit OTP
otp = random.randint(100000, 999999)
print("OTP:", otp)

# Random password of 10 characters
characters = string.ascii_letters + string.digits + "@#$%&*"
password = "".join(random.choices(characters, k=10))
print("Random password:", password)

# List of 5 random numbers between 1 and 100
random_list = [random.randint(1, 100) for _ in range(5)]
print("Random list:", random_list)
