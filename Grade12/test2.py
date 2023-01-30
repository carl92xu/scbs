file = open("prime.txt", "w")

for i in range(3, 1000, 2):
    not_prime = False

    for j in range(3, i+1//2):
        if i % j == 0:
            not_prime = True
            break

    if not_prime is False:
        file.write(str(i)+"\n")
        print(i)

file.close()
