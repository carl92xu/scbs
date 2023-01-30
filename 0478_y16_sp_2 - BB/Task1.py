StudentName = []
StudentTestMarks1 =[]
StudentTestMarks2 =[]
StudentTestMarks3 =[]
StudentTestMarksTotals =[]

def getName():
    name = input("Please type a student name")
    StudentName.append(name)

def getMark1():
    mark1 = int(input("Please enter the first mark (1-20)"))
    while mark1 not in range (0,21):
         mark1 = int(input("Please try again: enter the first mark (1-20)"))
    StudentTestMarks1.append(mark1)

def getMark2():
    mark2 = int(input("Please enter the second mark (1-25)"))
    while mark2 not in range (0,26):
         mark2 = int(input("Please try again: enter the second mark (1-25)"))
    StudentTestMarks2.append(mark2)

def getMark3():
    mark3 = int(input("Please enter the third mark (1-35)"))
    while mark3 not in range (0,36):
         mark3 = int(input("Please try again: enter the third mark (1-35)"))
    StudentTestMarks3.append(mark3)

for i in range(0,3):
    getName()
    getMark1()
    getMark2()
    getMark3()

print(StudentName)