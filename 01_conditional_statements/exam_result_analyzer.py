# Exam Result Analyzer (5 subjects, each out of 100)
# Fail if any subject < 33
# Division: >= 60% First, 50-59 Second, 40-49 Third

marks = []
for i in range(1, 6):
    marks.append(float(input(f"Enter marks of subject {i}: ")))

if min(marks) < 33:
    print("Result: Fail (scored below 33 in at least one subject)")
else:
    percentage = sum(marks) / 5
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 60:
        print("Division: First")
    elif percentage >= 50:
        print("Division: Second")
    elif percentage >= 40:
        print("Division: Third")
    else:
        print("Result: Pass (no division)")
