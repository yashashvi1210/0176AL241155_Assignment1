# Class with a private variable (__salary)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary        # private: can't be used directly from outside

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary must be positive!")

emp = Employee("Amit", 50000)
print("Salary:", emp.get_salary())
emp.set_salary(60000)
print("Updated salary:", emp.get_salary())

# print(emp.__salary)   # <- this would give an AttributeError
