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

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


dev_1 = Developer("Corey", "Shafer", 50000, "Python")
dev_2 = Developer("Test", "User", 60000, "Java")

# print(help(Developer))

print(dev_1.email, dev_1.prog_lang)
