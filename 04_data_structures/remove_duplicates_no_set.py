# Remove duplicates from a list WITHOUT using set, keeping the original order

items = [1, 2, 2, 3, 4, 3, 5, 1]

result = []
for item in items:
    if item not in result:
        result.append(item)

print("Original:", items)
print("Without duplicates:", result)
