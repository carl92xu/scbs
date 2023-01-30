rate = input('What is your salary per hour?')
hours = input('What is your working hours per week?')
if float(hours) > 40:
    pay = float(rate)*40 + (float(hours)-40)*float(rate)*1.5
else:
    pay = float(rate)*float(hours)
print(pay)