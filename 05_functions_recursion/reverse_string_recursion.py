# Reverse a string using recursion

def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]

word = input("Enter a string: ")
print("Reversed:", reverse(word))
