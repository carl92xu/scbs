rate = float(input('What is your salary per hour?'))
hours = float(input('What is your working hours per week?'))
def computepay(rate,hours):
    if hours > 40:
        pay = rate*40 + (hours-40)*rate*1.5
    else:
        pay = rate*hours
    return pay
print(computepay(rate,hours))