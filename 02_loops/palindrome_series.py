# Print all palindrome numbers in a given range

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Palindrome numbers:")
for num in range(start, end + 1):
    if str(num) == str(num)[::-1]:
        print(num, end=" ")
print()
