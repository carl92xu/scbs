#  By Carl
#  Starting from 2017.12.5 9am

#Functions
def menu():
    print("************************************************************")
    print("***                        ",turn+1,"                           ***")
    print("***                      Welcome                         ***")
    print("************************************************************")
    print("**                                                        **")
    print("** type STATS to count weekly yield                       **")
    print("** type TOTAL to count a cow's total yield                **")
    print("** type AVERAGE to count a cow's average yield for a week **")
    print("** type HIGHEST to identify the most productive cow       **")
    print("** type LESS to identify the cows have low yields         **")
    print("** type EXIT to quit                                      **")
    print("**                                                        **")
    print("************************************************************")

def per_yield(a):
    file = open("txtfile/cows.txt","r")
    cow_yield = 0
    for line in file:
        words = line.split(":")
        if words[0] == a:
            cow_yield = cow_yield + int(words[2])
    cow_yield = round(cow_yield)
    return(cow_yield)
    file.close()

def milk(a,b,c,d,e):
    file = open("txtfile/cows.txt","a")
    file.write(a+":"+str(b)+":"+str(c)+":"+str(d)+":"+e+":\n")
    file.close()
    print(a+":"+str(b)+":"+str(c)+":"+str(d)+":"+e+":")
    print("That record has been added")

def number_of_time_milked(a):
    file = open("txtfile/cows.txt","r")
    count = 0
    for line in file:
        words = line.split(":")
        if words[0] == a:
            count = count + 1
    return(count)
    file.close()

def quit():
    print("**************")
    print("**          **")
    print("** GOOD BYE **")
    print("**          **")
    print("**************")

def weekly_yield():
    file = open("txtfile/cows.txt", "r")
    wy = 0
    week = input("In which week?(eg.1,2,3,4...)\n--->")
    week = detect_week(week)
    week = str(int(week))
    for line in file:
        words=line.split(":")
        if words[1] == week:
            words = line.split(":")
            wy = wy + int(words[2])
    wy = round(wy)
    print("Total weekly yield is",wy)
    file.close

def average(a,b):
    file = open("txtfile/cows.txt", "r")
    cow_yield = 0
    times = 0
    for line in file:
        words = line.split(":")
        if words[0] == a:
            if words[1] == b:
                times = number_of_time_milked(a)
                cow_yield = cow_yield + int(words[2])
    if times == 0:
        print("No record")
        average_yield = "a"
    else:
        average_yield = cow_yield / times
        average_yield = round(average_yield)
    return(average_yield)
    file.close()

def cow_num():
    file = open("txtfile/cows.txt", "r")
    hci=[]
    for line in file:
        words = line.split(":")
        if int(words[0]) not in hci:
            hci.append(int(words[0]))
        else:
            continue
    hest=max(hci)
    return(hest)
    file.close()

def highest(a):
    high=[]
    for i in range(0,cow_num()):
        count=0
        file = open("txtfile/cows.txt", "r")
        for line in file:
            words = line.split(":")
            if int(words[0]) == i+1:
                if words[1] == a:
                    count = count + int(words[2])
        if count != 0:
            high.append(count)
    file.close()
    cdd = 0
    for j in range(len(high)):
        if max(high) == high[j]:
            cd=j+1
            if len(str(cd)) == 1:
                cdd="00"+str(cd)
            elif len(str(cd)) == 2:
                cdd="0"+str(cd)
            elif len(str(cd)) == 3:
                cdd=str(cd)
    return(cdd)

def less12():
    cow_has_rec = []
    less_than_12 = []
    week = input("Which week?(eg.1,2,3,4...)\n--->")
    week = detect_week(week)
    week = str(int(week))
    for i in range(0,cow_num()):
        file = open("txtfile/cows.txt", "r")
        ave = []
        for j in range(1, 8):
            count = 0
            for line in file:
                file = open("txtfile/cows.txt", "r")
                words = line.split(":")
                if int(words[0]) == i+1:
                    if words[1] == week:
                        if int(words[3]) == j:
                            count = count + int(words[2])
            if not (count == 0):
                ave.append(count)
        if not ave == []:
            cow_has_rec.append(i + 1)
        cc=0
        if len(ave) >= 4:
            for k in range(len(ave)):
                if ave[k] < 12:
                    cc = cc + 1
                if cc >= 4:
                    less_than_12.append("00"+str(i+1))
                    break
    file.close()
    if cow_has_rec != []:
        if less_than_12 == []:
            print("No cow has a yield lower than 12 for at least 4 days in this week")
    elif cow_has_rec == []:
        print("This week has no record")
    return(less_than_12)

def detect_cowID_shatl(a):
    if a.isdigit():
        if int(a) >= 1:
            if int(a) <= 999:
                detect = False
            else:
                detect = True
        else:
            detect = True
    else:
        detect = True

    while detect == True:

        if (a == "TOTAL") or (a == "total"):
            break
        elif (a == "STATS") or (a == "stats"):
            break
        elif (a == "AVERAGE") or (a == "average"):
            break
        elif (a == "HIGHEST") or (a == "highest"):
            break
        elif (a == "LESS") or (a == "less"):
            break

        print("Please input number 001~999")
        a = input("Which cow milked?(001~999)\n--->")
        if a.isdigit():
            if int(a) >= 1:
                if int(a) <= 999:
                    detect = False

    if len(str(a)) == 1:
        a = "00" + str(a)
    elif len(str(a)) == 2:
        a = "0" + str(a)
    elif len(str(a)) == 3:
        a = str(a)
    return(a)

def detect_cowID(a):
    if a.isdigit():
        if int(a) >= 1:
            if int(a) <= 999:
                detect = False
            else:
                detect = True
        else:
            detect = True
    else:
        detect = True

    while detect == True:

        print("Please input number 001~999")
        a = input("Which cow milked?(001~999)\n--->")
        if a.isdigit():
            if int(a) >= 1:
                if int(a) <= 999:
                    detect = False

    if len(str(int(a))) == 1:
        a = "00" + str(int(a))
    elif len(str(int(a))) == 2:
        a = "0" + str(int(a))
    elif len(str(int(a))) == 3:
        a = str(int(a))
    return(a)

def detect_week(a):
    if a.isdigit():
        detect = False
    else:
        detect = True
    while detect == True:
        print("Please input number like 1,2,3,4...")
        a = input("In which week?(eg.1,2,3,4...)\n--->")
        if a.isdigit():
            detect = False
    a = int(a)
    return(a)


#Code starts here
turn=0
menu()
cowID = input("Which cow milked?(001~999)\n--->")
cowID = detect_cowID_shatl(cowID)

while not (cowID == "EXIT" or  cowID == "exit"):
    if (cowID == "TOTAL") or (cowID == "total"):
        cowID = input("Which cow do you wish to count?(001~999)\n--->")
        cowID = detect_cowID(cowID)
        print(cowID,"milked",per_yield(cowID),"in",number_of_time_milked(cowID),"times")
    elif (cowID == "STATS") or (cowID == "stats"):
        weekly_yield()
    elif (cowID == "AVERAGE") or (cowID == "average"):
        cowwwID = input("Which cow?(001~999)\n--->")
        cowwwID = detect_cowID(cowwwID)
        week = input("In which week?(eg.1,2,3,4...)\n--->")
        week = detect_week(week)
        week = str(int(week))
        if average(cowwwID,week) != "a":
            print(cowwwID+"'s average yield for this week is",average(cowwwID,week),"each time")
    elif (cowID == "HIGHEST") or (cowID == "highest"):
        week = input("Which week?\n--->")
        week = detect_week(week)
        week = str(int(week))
        if highest(week) == 0:
            print("This week has no record")
        else:
            print("The most productive cow is", highest(week),"in this week")
    elif (cowID == "LESS") or (cowID == "less"):
        for item in less12():
            print(item,"has a yield lower than 12 for at least 4 days in this week")
    else:
        week = input("In which week?(eg.1,2,3,4...)\n--->")
        week = detect_week(week)

        day = input("In which day?(1~7)\n--->")
        #detect day
        if day.isdigit():
            if int(day) >= 1:
                if int(day) <= 7:
                    detect = False
                else:
                    detect = True
            else:
                detect = True
        else:
            detect = True
        while detect == True:
            print("Please input number 1~7")
            day = input("In which day?(1~7)\n--->")
            if day.isdigit():
                if int(day) >= 1:
                    if int(day) <= 7:
                        detect = False
        day = int(day)

        ap = input("On the morning(a) or afternoon(p)?\n--->")
        #detect ap
        if ap == "a":
            detect = False
        elif ap == "p":
            detect = False
        else:
            detect = True
        while detect == True:
            print("Please input 'a' or 'p'")
            ap = input("On the morning(a) or afternoon(p)?\n--->")
            if ap == "a":
                detect = False
            elif ap == "p":
                detect = False

        #detect repetition
        file = open("txtfile/cows.txt", "r")

        for line in file:
            words = line.split(":")
            if words[0] == cowID:
                if words[1] == str(week):
                    if words[3] == str(day):
                        if words[4] == ap:
                            print("This record has already been added, please check it")
                            break
        else:
                print ("How much did",cowID,"milk?")
                milk_data = input("--->")

                # detect milk_data
                if milk_data.isdigit():
                    if int(cowID) >= 0:
                        detect = False
                    else:
                        detect = True
                else:
                    detect = True
                while detect == True:
                    print("Please input number >= 0")
                    milk_data = input("--->")
                    if milk_data.isdigit():
                        if int(cowID) >= 0:
                            detect = False

                milk(cowID,int(week),int(milk_data),int(day),ap)
                #break
    turn = turn+1
    print("\n")
    menu()
    cowID = input("Which cow milked?(001~999)\n--->")
    cowID = detect_cowID_shatl(cowID)
quit()