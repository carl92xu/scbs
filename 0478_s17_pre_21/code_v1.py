CoachCost = 550
AnTicketCost = 30
while True:
    StudentNumber = int(input("Max Number of Student is 45, Please Input:"))
    if StudentNumber < 1:
        print("It should at least be 1")
    elif StudentNumber > 45:
        print("It should less than 45")
    elif StudentNumber in range(1,46):
        break
FreeTicketNumber = int(StudentNumber / 10)
TicketCost = (StudentNumber - FreeTicketNumber) * AnTicketCost
EstTotalCost = CoachCost + TicketCost
EstAveCost = round(EstTotalCost / StudentNumber,2)
print("The cost of each student is $" + str(EstAveCost))


Names = []
Paid_Not = []
Not = []
Paid = []
count = 0
for i in range(1,(StudentNumber+1)):
    print("i:",i)
    StudentName = input("Please input student name:")
    Names.append(StudentName)
    print("Paid or not(Input y or n)")
    PaidOrNot = input("Please input student paid or not:")
    Paid_Not.append(PaidOrNot)
for item in Paid_Not:
    if item == "n":
        Not.append(Names[count])
    elif item == "y":
        Paid.append(Names[count])
    count = count + 1
print("Paid:",Paid)
print("Not Paid:",Not)


print("\n")
while True:
    StudentNumber = int(input("Max Number of Student is 45, Please Input:"))
    if StudentNumber < 1:
        print("It should at least be 1")
    elif StudentNumber > 45:
        print("It should less than 45")
    elif StudentNumber in range(1,46):
        break
Names = []
Paid_Not = []
Not = []
Paid = []
count = 0
for i in range(1,(StudentNumber+1)):
    print("i:",i)
    StudentName = input("Please input student name:")
    Names.append(StudentName)
    print("Paid or not(Input y or n)")
    PaidOrNot = input("Please input student paid or not:")
    Paid_Not.append(PaidOrNot)
for item in Paid_Not:
    if item == "n":
        Not.append(Names[count])
    elif item == "y":
        Paid.append(Names[count])
    count = count + 1
print("Paid:",Paid)
print("Not Paid:",Not)
CollectedMoney = (len(Paid) +1) * EstAveCost
Final = EstTotalCost - CollectedMoney
print("Final:",round(Final,2))