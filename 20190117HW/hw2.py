tempC=int(input("Enter the temperature:"))
if tempC <= 0:
    print("It's frozen.")
elif tempC > 0 and tempC < 100:
    print("It's liquid.")
else:
    print("It's boiling.")