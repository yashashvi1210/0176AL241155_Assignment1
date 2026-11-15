# Find the missing number in a list that has numbers from 1 to n (one is missing)

numbers = [1, 2, 3, 5, 6]

n = len(numbers) + 1                 # total numbers there should be
expected_sum = n * (n + 1) // 2      # sum of 1..n
actual_sum = sum(numbers)

print("Missing number:", expected_sum - actual_sum)
