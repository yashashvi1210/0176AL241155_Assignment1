# Compress a string: "aaabbc" -> "a3b2c1"

text = input("Enter a string: ")

compressed = ""
i = 0
while i < len(text):
    count = 1
    while i + count < len(text) and text[i + count] == text[i]:
        count += 1
    compressed += text[i] + str(count)
    i += count

print("Compressed:", compressed)
