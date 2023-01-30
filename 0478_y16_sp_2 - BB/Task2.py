StudentName = []
StudentTestMarks1 =[]
StudentTestMarks2 =[]
StudentTestMarks3 =[]
StudentTestMarksTotals =[]

#getName  gets the name of the student, and appends it to the list StudentName
def getName():
    name = input("Please type a student name")
    StudentName.append(name)

#getMark1  gets the First mark (validates it in range) appends it to the end of list that stores that mark
def getMark1():
    mark1 = int(input("Please enter the first mark (1-20)"))
    while mark1 not in range (0,21):
         mark1 = int(input("Please try again: enter the first mark (1-20)"))
    StudentTestMarks1.append(mark1)

#getMark2  gets the First mark (validates it in range) appends it to the end of list that stores that mark
def getMark2():
    mark2 = int(input("Please enter the second mark (1-25)"))
    while mark2 not in range (0,26):
         mark2 = int(input("Please try again: enter the second mark (1-25)"))
    StudentTestMarks2.append(mark2)

#getMark3  gets the First mark (validates it in range) appends it to the end of list that stores that mark
def getMark3():
    mark3 = int(input("Please enter the third mark (1-35)"))
    while mark3 not in range (0,36):
         mark3 = int(input("Please try again: enter the third mark (1-35)"))
    StudentTestMarks3.append(mark3)

#calcTotal loops through each of the three marks for each student and totals them, it appends that total onto the appropriate list
def calcTotal():
    for i in range (0,3):
        totals = StudentTestMarks1[i]+StudentTestMarks2[i]+StudentTestMarks3[i]
        StudentTestMarksTotals.append(totals)

def calcClassAve():
    classTotal = 0
    classAverage = 0
    for i in range (0,3):
        classTotal = classTotal + StudentTestMarksTotals[i]
    classAverage = classTotal / 3
    return(classAverage)

for i in range(0,3):
    getName()
    getMark1()
    getMark2()
    getMark3()

calcTotal()

for i in range(0,3):
    print ('Student name: ',StudentName[i],' Total Score: ',StudentTestMarksTotals[i])

calcClassAve()
print('The Class Average Score is: ',calcClassAve())