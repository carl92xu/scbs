stu_name = []
test1 = []
test2 = []
test3 = []
total_score=[]
class_total=0
count = 0

for i in range(2):
    print("Student No."+str(i+1))
    name = input("Please enter student's name:")
    stu_name.append(name)
    mark1 = input("Please enter the student's mark for Test1:")
    test1.append(mark1)
    mark2 = input("Please enter the student's mark for Test2:")
    test2.append(mark2)
    mark3 = input("Please enter the student's mark for Test3:")
    test3.append(mark3)
    total_mark=int(mark1)+int(mark2)+int(mark3)
    total_score.append(total_mark)
    print("\n")

for item in total_score:
    print(stu_name[count]+":",item)
    count = count + 1

for item in total_score:
    class_total=class_total+int(item)
print("class_total",class_total)

print("length",len(total_score))
whole_class_average=class_total/len(total_score)
print("average",whole_class_average)
