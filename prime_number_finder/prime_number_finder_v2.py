import time
file = open("txtfile/prime.txt","r")
for line in file:
    words = line.split("\n")
    targetLine = words[-2]
print("Starting with:",targetLine)
file.close()
print("Used",str(time.process_time())+"s to get the number\n")
n1 = int(targetLine)
num = int(targetLine) + 1
count = 1
result = 0
time1 = time.time()
while True:
    if count < num:
        count = count + 1
    if num == count:
        if result == 0:
            n2 = num
            print("Difference:",n2-n1)
            n1 = num
            time2 = time.time()
            print("Used",str(time2 - time1)+"s\n")
            time1 = time.time()
            file = open("txtfile/prime.txt", "a")
            file.write(str(num)+"\n")
            file.close()
        num = num + 1
        count = 2
        result = 0
    if num%count == 0:
        result = 1
        num = num + 1
        count = 1
        result = 0
