class Employee:
    """This is Employee Class"""
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@company.com"


emp_1 = Employee("Corey", "Shafer", 50000)
emp_2 = Employee("Test", "User", 5000)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)
