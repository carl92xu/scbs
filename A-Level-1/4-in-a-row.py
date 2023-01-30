symbol=['','*','#']
board=[['0']*6,['0']*6,['0']*6,['0']*6,['0']*6,['0']*6]

def showBoard():
    for i in range(0,len(board)):
        print(board[i])

def checkRows(player):
    ply_symbol = symbol[int(player)]
    for i in range(0, 6):
        count = 0
        for j in range(0, 6):
            if board[i][j] == ply_symbol:
                count+=1
            elif board[j][i]!=ply_symbol and count<4:
                count = 0
            if count == 4:
                print(player, 'win')
                print('r')
                return True
            else:
                return False

def checkColumns(player):
    ply_symbol = symbol[int(player)]
    for i in range(0,6):
        count=0
        for j in range(0,6):
            if board[j][i]==ply_symbol:
                count += 1
            elif board[j][i]!=ply_symbol and count<4:
                count=0
            if count == 4:
                print(player,'win')
                print('c')
                return True
            else:
                return False

def playersGo(a):
    playerSymbol=symbol[a]
    row=0
    column=int(input('Which column do you want to put:'))
    while column not in range(1,7):
        column = int(input('Please enter a number between 1~6:'))
    while board[0][column-1] != '0':
        column = int(input('The column is full, which column do you want to put:'))
        while column not in range(1, 7):
            column = int(input('Please enter a number between 1~6:'))
    while board[row][column-1] == '0':
        row += 1
        if row == len(board):
            break
    board[row-1][column-1]=playerSymbol


endGame = False
turns = 0
while endGame == False:
    ThisPlayer = turns % 2 + 1
    showBoard()
    print('Player:',ThisPlayer,', Symbol:',symbol[ThisPlayer])
    ThisPlayer = turns%2+1
    playersGo(ThisPlayer)
    print('\n')
    endGame = checkRows(ThisPlayer)
    if endGame == False:
        endGame = checkColumns(ThisPlayer)
    turns += 1