class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def __check_pin(self, pin):
        return pin == self.__pin

    def check_balance(self, pin):
        if self.__check_pin(pin):
            print("Balance: ₹", self.__balance)
        else:
            print("Wrong PIN!")

    def deposit(self, pin, amount):
        if not self.__check_pin(pin):
            print("Wrong PIN!")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.__balance += amount
            print(f"₹{amount} deposited.")

    def withdraw(self, pin, amount):
        if not self.__check_pin(pin):
            print("Wrong PIN!")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn.")

atm = ATM(pin=1234, balance=10000)

while True:
    print("\n1. Balance  2. Deposit  3. Withdraw  4. Exit")
    choice = input("Choose: ")
    if choice == "4":
        print("Thank you!")
        break
    pin = int(input("Enter PIN: "))
    if choice == "1":
        atm.check_balance(pin)
    elif choice == "2":
        atm.deposit(pin, int(input("Amount: ")))
    elif choice == "3":
        atm.withdraw(pin, int(input("Amount: ")))
    else:
        print("Invalid choice.")
