class UnderAgeError(Exception):
    pass

def validate_age(age):
    if age < 18:
        raise UnderAgeError("Age must be 18 or above!")
    return "Age is valid. Access granted."

try:
    age = int(input("Enter your age: "))
    print(validate_age(age))
except UnderAgeError as e:
    print("Error:", e)
except ValueError:
    print("Error: please enter a number.")
