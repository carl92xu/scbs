file = open("txtfile/prime.txt","r")
for line in file:
    words = line.split("\n")
    targetLine = words[-2]
print("Starting with:",targetLine)
file.close()
num = int(targetLine) + 1
count = 1
result = 0
while True:
    if count < num:
        count = count + 1
    if num == count:
        if result == 0:
            file = open("txtfile/prime.txt", "a")
            file.write(str(num)+"\n")
            file.close()
        num = num + 1
        count = 2
        result = 0
    if num%count == 0:
        num = num + 1
        count = 1