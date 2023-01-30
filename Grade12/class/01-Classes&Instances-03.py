class Employee:
    """This is Employee Class"""
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@company.com"

    def fullname(self):
        fullname = "{} {}".format(self.first, self.last)
        return fullname


emp_1 = Employee("Corey", "Shafer", 50000)
emp_2 = Employee("Test", "User", 5000)

print(emp_1)
print(emp_2)

print(emp_1.fullname())  # this is the same as
print(Employee.fullname(emp_1))
print(emp_2.fullname())
