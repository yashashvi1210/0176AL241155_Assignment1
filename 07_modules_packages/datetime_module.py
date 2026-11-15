from datetime import datetime, date

now = datetime.now()
print("Current date and time:", now.strftime("%d-%m-%Y %H:%M:%S"))

dob_text = input("Enter your date of birth (DD-MM-YYYY): ")
dob = datetime.strptime(dob_text, "%d-%m-%Y").date()
today = date.today()

age = today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1          # birthday hasn't come yet this year

print("Your age is:", age, "years")
