count = 0
num = 0
nextNum = float(input("num"+str(count+1)))
while nextNum != 0:
    num += nextNum
    count += 1
    nextNum = float(input("num"+str(count+1)))
print(num/count)