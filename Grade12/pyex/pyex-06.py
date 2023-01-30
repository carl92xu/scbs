def ISBNcheck(ISBN):

    # Split the ISBN into the Unique ID and the check digit
    unique_id = []
    for i in range(len(ISBN)-1):
        unique_id.append(int(ISBN[i]))
    actual_check_digit = int(ISBN[-1])

    # Multiply the second, forth, sixth, ... elements by three
    times_three = []
    for x in range(len(unique_id)):
        if (x+1) % 2 == 0 and x != 0:
            times_three.append(unique_id[x]*3)
        else:
            times_three.append(unique_id[x])

    # Calculate the sum of the numbers
    sum_new_digits = sum(times_three)

    # Take the sum mod 10, and subtract from 10
    sum_mod_10 = sum_new_digits % 10
    if sum_mod_10 == 0:
        sum_mod_10 = 10
    check_digit = 10 - sum_mod_10

    # Check that the calculated check digit is equal to the given check digit
    if check_digit == actual_check_digit:
        return True
    else:
        print(check_digit)
        return False
        

def country_check(ISBN):
    country_code = int(ISBN[3])
    if country_code == 0:
        return "A"
    elif country_code == 1:
        return "B"
    elif country_code == 2:
        return "C"
    elif country_code == 3:
        return "D"
    elif country_code == 4:
        return "E"
    else:
        return "Invalid country code"


# choice = input("Enter the ISBN number: ")
choice = str(9781471117909)
while len(choice) != 13:
    choice = input("ISBN number need to be 13 digits: ")

first_three = choice[0:3]
if first_three == "978":
    check = ISBNcheck(choice)
    print(check)
    print(country_check(choice))
else:
    print("The ISBN number is invalid.")
