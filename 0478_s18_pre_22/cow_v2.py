#  By Carl
#  Starting from 2018.4.23 14:41

#Functions
def menu():
    print("************************************************************")
    print("***                      Welcome                         ***")
    print("************************************************************")
    print("**                                                        **")
    print("** type WEEK to count weekly yield                       **")
    print("** type AVERAGE to count a cow's average yield for a week **")
    print("** type HIGHEST to identify the most productive cow       **")
    print("** type LESS to identify the cows have low yields         **")
    print("** type EXIT to quit                                      **")
    print("**                                                        **")
    print("************************************************************",'\n')

def quit():
    print("**************")
    print("**          **")
    print("** GOOD BYE **")
    print("**          **")
    print("**************")

def record(a,b,c,d):
    if c == 'am':
        amMilking[int(a)*int(b)-1] = d
    elif c == 'pm':
        pmMilking[int(a)*int(b)-1] = d

def week():
    for i in amMilking:
        WeekTot = WeekTot + amMilking[i] + pmMilking[i]
    print(WeekTot)

def average(a):
    a = int(a)
    ave = 0
    for i in range(0,7):
        print('i',i)
        CowYield = amMilking[i*a] + pmMilking[i*a]
    ave = CowYield/14
    print(ave)

def highest():
    for i in range(0,5):
        print('i',i)
        counter = 0
        for j in range(0,5):
            print('j',j)
            counter = counter + amMilking[i*j] + pmMilking[i*j]
            print(counter)
        Highest.append(counter)
    print(max(Highest)+1)

def less(a):
    for i in range(0,5):
        print('i',i)
        count = []
        for j in range(0,6):
            print('j',j)
            CowYield = 0
            CowYield = amMilking[i*a] + pmMilking[i*a]
            ave = CowYield / 2
            if ave < 12:
                count.appand(ave)
        if len(count) >= 4:
            Less.append(a)
    print(Less,'have a low yield')

def add_am():
    myfile = open("amMilking.txt","r")
    for i in range (0,milkYields):
        amMilking[i] = round(float(myfile.readline().rstrip('\n')),1)
    myfile.close()

def add_pm():
    myfile = open("pmMilking.txt","r")
    for i in range (0,milkYields):
        pmMilking[i] =round(float(myfile.readline().rstrip('\n')),1)
    myfile.close()

#Code starts here
amMilking = []
pmMilking = []
Less = []
Highest = []
cowIdentity =[]
WeekTot = 0
milkYields = 35

for i in range(0,35):
    amMilking.append(0)
    pmMilking.append(0)


add_am()
add_pm()
print("\n"+"cow Identities: ",cowIdentity)
print("am Yields: ",amMilking)
print("pm Yields: ",pmMilking,"\n")


menu()
CowID = input('Please enter Cow ID:')
while CowID != 'exit':
    if CowID == 'week':
        week()
    elif CowID == 'average':
        CowID = input('Please enter Cow ID:')
        average(str(CowID))
    elif CowID == 'highest':
        highest()
    elif CowID == 'less':
        less(CowID)
    else:
        Day = input('In which day:')
        ap = input('AM or PM:')
        Yield = input("What's the yield:")
        record(CowID,Day,ap,Yield)
        print(amMilking)
        print(pmMilking)
        menu()
        CowID = input('Please enter Cow ID:')
quit()