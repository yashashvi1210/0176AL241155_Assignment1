# Password Validator with custom exceptions:
# a) length < 8   b) no uppercase letter   c) no number

class PasswordTooShortError(Exception):
    pass

class NoUppercaseError(Exception):
    pass

class NoNumberError(Exception):
    pass

def validate_password(password):
    if len(password) < 8:
        raise PasswordTooShortError("Password must be at least 8 characters long.")
    if not any(ch.isupper() for ch in password):
        raise NoUppercaseError("Password must contain at least one uppercase letter.")
    if not any(ch.isdigit() for ch in password):
        raise NoNumberError("Password must contain at least one number.")
    return "Strong password!"

pwd = input("Enter a password: ")
try:
    print(validate_password(pwd))
except (PasswordTooShortError, NoUppercaseError, NoNumberError) as e:
    print("Invalid password:", e)
