myfile=open('data.txt','r')

i=myfile.readline()
while i !='':
    i = myfile.readline()
    print(i)

myfile.close()


myfile=open('data.txt','r')
print(myfile.tell())




myfile.close()