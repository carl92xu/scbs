r1=[' ',' ',' ']
r2=[' ',' ',' ']
r3=[' ',' ',' ']

print(str(r1)+"\n"+str(r2)+"\n"+str(r3)+"\n")

while True:
#Player1
    plc1=input("P1 Enter C")
    plc2=input("P1 Enter R")
    while True:
        if plc1 == '1' and r1[int(plc2)-1] == " ":
            r1[int(plc2)-1] = "X"
            break
        elif r1[int(plc2) - 1] != " ":
            print("Error")
            break
        if plc1 == '2' and r2[int(plc2)-1] == " ":
            r2[int(plc2)-1] = "X"
            break
        elif r1[int(plc2) - 1] != " ":
            print("Error")
            break
        if plc1 == 'MyPycharm3' and r2[int(plc2)-1] == " ":
            r3[int(plc2)-1] = "X"
            break
        elif r3[int(plc2) - 1] != " ":
            print("Error")
            break

    print(str(r1) + "\n" + str(r2) + "\n" + str(r3) + "\n")

#Player2
    pllc1 = input("P2 Enter C")
    pllc2 = input("P2 Enter R")
    while True:
        while pllc1 == '1' and r1[int(pllc2)-1] == " ":
            r1[int(pllc2)-1] = "O"
            break
        else:
            if r1[int(pllc2) - 1] != " ":
                print("Error")
                pllc1 = input("P2 Enter C")
                pllc2 = input("P2 Enter R")
                if True:
                    break
        if pllc1 == '2' and r2[int(pllc2)-1] == " ":
            r2[int(pllc2)-1] = "O"
            break
        elif r2[int(pllc2) - 1] != " ":
            print("Error")
            break
        if pllc1 == 'MyPycharm3' and r2[int(pllc2)-1] == " ":
            r3[int(pllc2)-1] = "O"
            break
        elif r1[int(pllc2) - 1] != " ":
            print("Error")
            break

    print(str(r1) + "\n" + str(r2) + "\n" + str(r3) + "\n")