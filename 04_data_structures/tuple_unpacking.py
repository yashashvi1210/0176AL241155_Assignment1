# Swap first and last elements of a tuple without converting it to a list

data = (10, 20, 30, 40, 50)

first, *middle, last = data          # unpack: first, middle part, last
swapped = (last, *middle, first)     # build a new tuple

print("Original:", data)
print("Swapped: ", swapped)
