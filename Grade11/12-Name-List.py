Name = []
Age = []
for i in range(3):
    n = input("Enter Student Name: ")
    Name.append(n)
    a = int(input("Enter "+n+"'s Age: "))
    Age.append(a)
print(Name, end='')
print(Age)