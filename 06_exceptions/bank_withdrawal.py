# Bank Withdrawal System: raise an exception if withdrawal exceeds balance

class InsufficientBalanceError(Exception):
    pass

balance = 5000

def withdraw(amount):
    global balance
    if amount > balance:
        raise InsufficientBalanceError(
            f"Cannot withdraw ₹{amount}. Available balance is ₹{balance}."
        )
    balance -= amount
    print(f"Withdrawal successful. New balance: ₹{balance}")

try:
    amount = int(input("Enter amount to withdraw: "))
    withdraw(amount)
except InsufficientBalanceError as e:
    print("Error:", e)
except ValueError:
    print("Error: please enter a valid number.")
