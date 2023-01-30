class Employee:
    """This is Employee Class"""


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)


'''We can manually create instance variables
Each of these instances have attributes that are unique to them'''
emp_1.first = "Corey"
emp_1.last = "Shafer"
emp_1.email = "Corey.Shafer@company.com"
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "Test.User@company.com"
emp_2.pay = 50000

print(emp_1.email)
print(emp_2.email)
