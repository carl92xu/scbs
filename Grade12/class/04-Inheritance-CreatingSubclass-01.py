class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        fullname = "{} {}".format(self.first, self.last)
        return fullname

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.1


dev_1 = Developer("Corey", "Shafer", 50000)
dev_2 = Developer("Test", "User", 60000)

# print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
