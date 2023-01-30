listoflist = [['0']*6,['0']*6,['0']*6,['0']*6,['0']*6,['0']*6,['0']*6]

for i in range(0,3):
    listoflist[i][i]='X'
    listoflist[i][-i-1]='X'
    listoflist[-i-2][i]='X'
    listoflist[-i-2][-i-1]='X'

for i in range(0,6):
    for j in range(0,6):
        print(listoflist[i][j],end='')
    print('')