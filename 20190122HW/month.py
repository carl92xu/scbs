month = str(input("Enter Month: "))
if month == str(1):
    print("31 Days")
elif month == str(2):
    year = int(input("Enter Year: "))
    if year % 4 == 0 and year % 100 != 0:
        print("29 Days")
    else:
        print("28 Days")
elif month == str(3):
    print("31 Days")
elif month == str(4):
    print("30 Days")
elif month == str(5):
    print("31 Days")
elif month == str(6):
    print("30 Days")
elif month == str(7):
    print("31 Days")
elif month == str(8):
    print("31 Days")
elif month == str(9):
    print("30 Days")
elif month == str(10):
    print("31 Days")
elif month == str(11):
    print("30 Days")
elif month == str(12):
    print("31 Days")
