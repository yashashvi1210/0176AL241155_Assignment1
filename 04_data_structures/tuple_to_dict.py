# Convert a tuple of pairs to a dictionary
# ((1, "A"), (2, "B")) -> {1: "A", 2: "B"}

pairs = ((1, "A"), (2, "B"), (3, "C"))

result = {}
for key, value in pairs:
    result[key] = value

print(result)
