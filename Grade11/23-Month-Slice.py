def monthNumberValidation(a):
    while a < 0 or a > 12:
        a = int(input("Please Enter Month Number Again: "))
    return a


monthName = "JanFebMarAprMayJunJulAugSepOctNovDec"
monthNumber = int(input("Month Number: "))
monthNumber = monthNumberValidation(monthNumber)
while monthNumber != 0:
    monthIndex = 3*monthNumber
    print(monthName[monthIndex-3:monthIndex])
    monthNumber = int(input("Month Number: "))
    monthNumber = monthNumberValidation(monthNumber)
print("END")

sample = "This is a sample string"
print(sample[:])

myList = [1, 2, 3, 4, -100]
mySubList = myList[3:5]
print(mySubList)