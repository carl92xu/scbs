num = 1
while num != 0:
    num = int(input("Number: "))
    for i in range(1, num):
        if num % i == 0:
            print(i)
    print()
