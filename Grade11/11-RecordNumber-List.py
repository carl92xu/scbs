import random
MyList = []
for i in range(0,7,1):
    #MyList.append(int(input("Input item"+str(i+1)+":")))
    MyList.append(i*random.random())
print(MyList)

for i in range(7):
    print(i,"       ",MyList[i])