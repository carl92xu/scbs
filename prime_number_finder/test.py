import time
num = 2

for i in range(77232917):
    if i % 1000000 == 0:
        print("i:",i)
        print("Used", str(time.process_time()) + "s")
    num = int(num) * 2

print("Used", str(time.process_time()) + "s")
print("num:",num)
print("Used", str(time.process_time()) + "s")

file = open("txtfile/test.txt", "w")
file.write(str(num))
file.close()
print("Used", str(time.process_time()) + "s")