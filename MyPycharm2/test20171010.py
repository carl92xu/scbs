myfile=open('data.txt','a')
un=input('Username:')
pw=input('PW:')
myfile.write(str(un+" "))
myfile.write(str(pw+"\n"))
myfile.close()

myfile=open('data.txt','r')

i=myfile.readline()
while i !='':
    i = myfile.readline()
    print(i)

myfile.close()