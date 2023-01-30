list = []
for i in range(5):
    list.append(i)
print(list)

list1 = ["Train","Car","Bus","Plane","Foot"]
list1.reverse()
print(list1)

list2 = [30,-5,77,50,100]
list2.sort()
print(list2)

list3 = []
list3.append("ABC")
print(list3)

list4 = ["Train","Car","Bus","Plane","Foot"]
list4.remove("Car")
print(list4)

list5 = ["Train", "Car", "Bus", "Plane", "Foot"]
index = list5.index("Car")
print("The index for 'Car' is",index)

list6 = ["Train", "Car", "Bus", "Plane", "Foot"]
list6.append("Car")
count = list6.count("Car")
print(count)

list7 = ["Train", "Car", "Bus", "Plane", "Foot"]
list7.insert(1, "Car")
print(list7)

list8 = ["Train", "Car", "Bus", "Plane", "Foot"]
list8.pop(0)
print(list8)