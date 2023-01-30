r1=[' ',' ',' ']
r2=[' ',' ',' ']
r3=[' ',' ',' ']
print(str(r1)+"\n"+str(r2)+"\n"+str(r3)+"\n")

while True:

#Player1
    plc1=input("P1 Enter C")
    plc2=input("P1 Enter R")
    while True:
        if plc1 == '1':
            r1[int(plc2)-1]="X"
            break
        elif plc1 == '2':
            r2[int(plc2)-1]="X"
            break
        elif plc1 == 'MyPycharm3':
            r3[int(plc2)-1]="X"
            break

    print(str(r1) + "\n" + str(r2) + "\n" + str(r3) + "\n")

#Player2
#while True? Then add 'break's?

    pllc1 = input("P2 Enter C")
    pllc2 = input("P2 Enter R")
    while True:
        if pllc1 == '1':
            r1[int(pllc2) - 1] = "O"
            break
        elif pllc1 == '2':
            r2[int(pllc2) - 1] = "O"
            break
        elif pllc1 == 'MyPycharm3':
            r3[int(pllc2) - 1] = "O"
            break

    print(str(r1) + "\n" + str(r2) + "\n" + str(r3) + "\n")