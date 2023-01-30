r1 = [' ', ' ', ' ']
r2 = [' ', ' ', ' ']
r3 = [' ', ' ', ' ']

print(str(r1) + "\n" + str(r2) + "\n" + str(r3) + "\n")

while True:
    plc1 = input("P1 Enter C")
    plc2 = input("P1 Enter R")
    while True:
#plc 1
        if plc1 == '1':
            if r1[int(plc2) - 1] == ' ':
                r1[int(plc2) - 1] = "X"
                break
            else:
                print("Error")
                plc1 = input("P1 Enter C")
                plc2 = input("P1 Enter R")

                if plc1 == '1' and r1[int(plc2) - 1] == ' ':
                    r1[int(plc2) - 1] = "X"
                    break
                elif plc1 == '2' and r2[int(plc2) - 1] == ' ':
                    r2[int(plc2) - 1] = "X"
                    break
                elif plc1 == 'MyPycharm3' and r3[int(plc2) - 1] == ' ':
                    r3[int(plc2) - 1] = "X"
                    break
                else:
                    print("Error")
                    break
#plc 2
        if plc1 == '2':
            if r2[int(plc2) - 1] == ' ':
                r2[int(plc2) - 1] = "X"
                break
            else:
                print("Error")
                plc1 = input("P1 Enter C")
                plc2 = input("P1 Enter R")

                if plc1 == '1' and r1[int(plc2) - 1] == ' ':
                    r1[int(plc2) - 1] = "X"
                    break
                elif plc1 == '2' and r2[int(plc2) - 1] == ' ':
                    r2[int(plc2) - 1] = "X"
                    break
                elif plc1 == 'MyPycharm3' and r3[int(plc2) - 1] == ' ':
                    r3[int(plc2) - 1] = "X"
                    break
                else:
                    print("Error")
                    break

#plc MyPycharm3
        if plc1 == 'MyPycharm3':
            if r3[int(plc2) - 1] == ' ':
                r3[int(plc2) - 1] = "X"
                break
            else:
                print("Error")
                plc1 = input("P1 Enter C")
                plc2 = input("P1 Enter R")

                if plc1 == '1' and r1[int(plc2) - 1] == ' ':
                    r1[int(plc2) - 1] = "X"
                    break
                elif plc1 == '2' and r2[int(plc2) - 1] == ' ':
                    r2[int(plc2) - 1] = "X"
                    break
                elif plc1 == 'MyPycharm3' and r3[int(plc2) - 1] == ' ':
                    r3[int(plc2) - 1] = "X"
                    break
                else:
                    print("Error")
                    break

    print(str(r1) + "\n" + str(r2) + "\n" + str(r3) + "\n")

    while True:
#pllc 1
        pllc1 = input("P2 Enter C")
        pllc2 = input("P2 Enter R")
        while True:
            if pllc1 == '1':
                if r1[int(pllc2) - 1] == ' ':
                    r1[int(pllc2) - 1] = "O"
                    break
                else:
                    print("Error")
                    pllc1 = input("P2 Enter C")
                    pllc2 = input("P2 Enter R")

                    if pllc1 == '1' and r1[int(pllc2) - 1] == ' ':
                        r1[int(pllc2) - 1] = "O"
                        break
                    elif pllc1 == '2' and r2[int(pllc2) - 1] == ' ':
                        r2[int(pllc2) - 1] = "O"
                        break
                    elif pllc1 == 'MyPycharm3' and r3[int(pllc2) - 1] == ' ':
                        r3[int(pllc2) - 1] = "O"
                        break
                    else:
                        print("Error")
                        break
#pllc 2
            elif pllc1 == '1':
                if r2[int(pllc2) - 1] == ' ':
                    r2[int(pllc2) - 1] = "O"
                    break
                else:
                    print("Error")
                    pllc1 = input("P2 Enter C")
                    pllc2 = input("P2 Enter R")

                    if pllc1 == '1' and r1[int(pllc2) - 1] == ' ':
                        r1[int(pllc2) - 1] = "O"
                        break
                    elif pllc1 == '2' and r2[int(pllc2) - 1] == ' ':
                        r2[int(pllc2) - 1] = "O"
                        break
                    elif pllc1 == 'MyPycharm3' and r3[int(pllc2) - 1] == ' ':
                        r3[int(pllc2) - 1] = "O"
                        break
                    else:
                        print("Error")
                        break
#pllc MyPycharm3
            elif pllc1 == '1':
                if r3[int(pllc2) - 1] == ' ':
                    r3[int(pllc2) - 1] = "O"
                    break
                else:
                    print("Error")
                    pllc1 = input("P2 Enter C")
                    pllc2 = input("P2 Enter R")

                    if pllc1 == '1' and r1[int(pllc2) - 1] == ' ':
                        r1[int(pllc2) - 1] = "O"
                        break
                    elif pllc1 == '2' and r2[int(pllc2) - 1] == ' ':
                        r2[int(pllc2) - 1] = "O"
                        break
                    elif pllc1 == 'MyPycharm3' and r3[int(pllc2) - 1] == ' ':
                        r3[int(pllc2) - 1] = "O"
                        break
                    else:
                        print("Error")
                        break

        print(str(r1) + "\n" + str(r2) + "\n" + str(r3) + "\n")
        break