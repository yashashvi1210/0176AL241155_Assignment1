# Check whether one set is a subset of another

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

if a.issubset(b):
    print(f"{a} is a subset of {b}")
else:
    print(f"{a} is NOT a subset of {b}")
