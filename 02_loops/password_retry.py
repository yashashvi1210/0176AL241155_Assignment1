# Password Retry System: max 3 attempts, then blocked

correct_password = "python123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    entered = input("Enter password: ")
    if entered == correct_password:
        print("Access granted!")
        break
    attempts += 1
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"Wrong password. {remaining} attempt(s) left.")
else:
    print("Too many failed attempts. Account BLOCKED!")
