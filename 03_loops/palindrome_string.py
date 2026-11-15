# Palindrome String Check (ignore spaces and uppercase/lowercase)

text = input("Enter a string: ")
cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("It is a palindrome")
else:
    print("It is NOT a palindrome")
