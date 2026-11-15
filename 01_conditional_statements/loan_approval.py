# Loan Approval System
# Approved             -> salary >= 30000 AND credit score >= 700 AND age 21-60
# Conditionally Approved -> age is OK, but only ONE of (salary, credit score) is good
# Rejected             -> everything else

salary = float(input("Enter monthly salary (₹): "))
credit_score = int(input("Enter credit score: "))
age = int(input("Enter age: "))

if not (21 <= age <= 60):
    print("Rejected (age must be between 21 and 60)")
elif salary >= 30000 and credit_score >= 700:
    print("Approved")
elif salary >= 30000 or credit_score >= 700:
    print("Conditionally Approved")
else:
    print("Rejected")
