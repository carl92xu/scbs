StudentName = []
StudentTestMarks1 =[]
StudentTestMarks2 =[]
StudentTestMarks3 =[]
StudentTestMarksTotals =[]
maxStudents = 2   #I set this to 2 to make testing faster

#getName  gets the name of the student, and appends it to the list StudentName
def getName():
    name = input("\nPlease type a student name")
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
    for i in range (0,maxStudents):
        totals = StudentTestMarks1[i]+StudentTestMarks2[i]+StudentTestMarks3[i]
        StudentTestMarksTotals.append(totals)

#calcClassAve loops through the totals and calculates the average / number of students. It returns that value.
def calcClassAve():
    classTotal = 0
    classAverage = 0
    for i in range (0,maxStudents):
        classTotal = classTotal + StudentTestMarksTotals[i]
    classAverage = classTotal / maxStudents
    return(classAverage)

#findHighestStudent loops through the totals and finds the index for the stdent with the highest value. It returns that value.
def findHighestStudent():
    highestStudentIndex = 0
    for i in range (0,maxStudents):
        if StudentTestMarksTotals[i] > StudentTestMarksTotals[highestStudentIndex]:
            highestStudentIndex = i
    return(highestStudentIndex)

'''**********************************************************
The main program starts below
*************************************************************'''

for i in range(0,maxStudents):
    getName()
    getMark1()
    getMark2()
    getMark3()

#Call to def calcTotal
calcTotal()

print('\n---------------------------------------------\n')

#Outputs the name and totals for each Student
for i in range(0,maxStudents):
    print ('Student name: ',StudentName[i],' Achieved a total score of: ',StudentTestMarksTotals[i])

print('\n---------------------------------------------\n')

#Outputs the Class Average Score  (the definition returs the average so I can use the call in the output
print('The class average Score is: ',calcClassAve())

print('\n---------------------------------------------\n')

#Outputs the Student with the higest total, the deff returns the position in the lists of the name and total score
student = findHighestStudent() #this call the def that returns the index of the student with the higest total
print('Student: ',StudentName[student], 'achieved the highest total of: ',StudentTestMarksTotals[student])
print('\n---------------------------------------------')