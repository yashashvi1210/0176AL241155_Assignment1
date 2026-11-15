# List Rotation: rotate a list left or right by k positions

def rotate_left(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

def rotate_right(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k] if k else lst[:]

numbers = [1, 2, 3, 4, 5]
k = int(input("Rotate by how many positions (k)? "))
direction = input("Direction (left/right): ").lower()

if direction == "left":
    print("Result:", rotate_left(numbers, k))
elif direction == "right":
    print("Result:", rotate_right(numbers, k))
else:
    print("Please type 'left' or 'right'")
