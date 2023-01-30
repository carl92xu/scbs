set1 = [1,2,3,4,5,6,7,8,9,10]
set2 = [11,12,13,14,15,16,17,18,19,20]
set3 = [21,22,23,24,25,26,27,28,29,30]
set4 = [31,32,33,34,35,36,37,38,39,40]
set5 = [41,42,43,44,45,46,47,48,49,50]
set6 = [51,52,53,54,55,56,57,58,59,60]
set7 = [61,62,63,64,65,66,67,68,69,70]

Listoflist = [set1,set2,set3,set4,set5,set6,set7]

count = 0
i=0

while i < 7:
    sum = 0
    j = 0
    while j <10:
        sum = sum + Listoflist[count][j]
        j = j+1
    print (sum)
    count=count+1
    i=i+1
print("End")