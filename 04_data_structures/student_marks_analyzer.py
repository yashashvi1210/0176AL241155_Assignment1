# Student Marks Analyzer: topper, average, failures (pass mark = 33)

students = {
    "Aman": 78,
    "Riya": 92,
    "Karan": 30,
    "Sneha": 65,
    "Rohit": 28,
}

topper = max(students, key=students.get)
average = sum(students.values()) / len(students)
failures = [name for name, marks in students.items() if marks < 33]

print("Topper:", topper, "with", students[topper], "marks")
print("Class average:", average)
print("Failed students:", failures if failures else "None")
