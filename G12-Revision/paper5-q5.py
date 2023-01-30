def ValidMove(PieceColor, xCurrent, yCurrent, board):  # Horizontal Moves Only
    if (board[yCurrent][xCurrent+1] != PieceColor) or (board[yCurrent][xCurrent-1] != PieceColor):
        print("Possible moves are:")
        if board[yCurrent][xCurrent-1] != PieceColor:
            print("Moving LEFT")
            for i in range(xCurrent-1, -1, -1):
                if board[yCurrent][i] == PieceColor:
                    break
                else:
                    if board[yCurrent][i] == "E":
                        print(i+1, yCurrent+1)
                    else:
                        print(i+1, yCurrent+1, "REMOVE piece")
                        break
        if board[yCurrent][xCurrent+1] != PieceColor:
            print("Moving RIGHT")
            for i in range(xCurrent+1, 8):
                if board[yCurrent][i] == PieceColor:
                    break
                else:
                    if board[yCurrent][i] == "E":
                        print(i+1, yCurrent+1)
                    else:
                        print(i+1, yCurrent+1, "REMOVE piece")
                        break


def InitializeBoard(board):
    for i in range(8):
        board.append([])
        for j in range(8):
            if i == 0 or i == 1:
                board[i].append("B")
            elif 2 <= i <= 5:
                board[i].append("E")
            else:
                board[i].append("W")


myBoard = []
InitializeBoard(myBoard)

# Test
myBoard[3][3] = "B"
myBoard[3][1] = "W"
myBoard[3][7] = "B"
for row in myBoard:
    print(row)

print()
ValidMove("B", 3, 3, myBoard)
