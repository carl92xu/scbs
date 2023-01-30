def draw(grid):
    '''print("")
    print("1 2 3 4 5")  # Print column headers
    print("| | | | |")
    print(grid[0][0], grid[0][1], grid[0][2], grid[0][3], grid[0][4], "- row 1")
    print(grid[1][0], grid[1][1], grid[1][2], grid[1][3], grid[1][4], "- row 2")
    print(grid[2][0], grid[2][1], grid[2][2], grid[2][3], grid[2][4], "- row 3")
    print(grid[3][0], grid[3][1], grid[3][2], grid[3][3], grid[3][4], "- row 4\n")'''
    for c in range(len(grid[0])):
        print(c+1, end=" ")
    print()
    for c in range(len(grid[0])):
        print("| ", end="")
    print()
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            print(grid[r][c], end=" ")
        print("-", r+1, "\n", end="")


def add_piece(grid, column, player):
    if player == 1:
        piece = "B"
    else:
        piece = "R"
    
    if grid[len(grid)-1][column] == 0:
        grid[len(grid)-1][column] = piece
    else:
        for r in range(len(grid)):
            if grid[r][column] != 0:
                grid[r-1][column] = piece
                break
    return grid


def winner_check(grid, player):
    if player == 1:
        piece = "B"
    else:
        piece = "R"
    # horizontal check
    for i in range(len(grid)):
        hor_count = 0
        for j in range(len(grid[i])-4):
            for k in range(1, 5):
                if grid[i][j+k] == piece:
                    hor_count += 1
                else:
                    hor_count = 0
            if hor_count == 4:
                return True
    # vertical check
    for i in range(len(grid[0])):
        ver_count = 0
        for j in range(3, len(grid)-1):
            for k in range(4):
                if grid[j-k][i] == piece:
                    ver_count += 1
                else:
                    ver_count = 0
            if ver_count == 4:
                return True
    # not win yet
    return False


# not really finished
def winner_check_dia(grid, player):
    if player == 1:
        piece = "B"
    else:
        piece = "R"
    
    # diagnoal up
    for i in range(3, len(grid)):
        dia_up_count = 0
        for j in range(len(grid[i])):
            # continue
            for k in range(4):
                if grid[i+k][j+k] == piece:
                    dia_up_count += 1
                else:
                    dia_up_count = 0
            if dia_up_count == 4:
                return True
    
    # diagnoal down
    for i in range(len(grid)-4): # ???
        dia_up_count = 0
        for j in range(len(grid[i])):
            # continue
            for k in range(4):
                if grid[i-k][j-k] == piece:
                    dia_up_count += 1
                else:
                    dia_up_count = 0
            if dia_up_count == 4:
                return True
    
    return False

# Main Program
row_num = 9  # int(input("Board row size: "))
col_num = 9  # int(input("Board column size: "))
board = []

for i in range(row_num):
    board.append([])
    for j in range(col_num):
        board[i].append(0)

won = False

draw(board)
player = 2

while won is not True:

    if player == 1:
        player = 2
    else:
        player = 1

    print("It is player " + str(player) + "'s go.")
    c_choice = int(input("Enter the column number: "))-1
    
    try:
        while board[0][c_choice] != 0:
            c_choice = int(input("Invalid column, please re-enter: "))-1
    except:
        pass
    
    '''while not(0 <= c_choice <= 4):
        c_choice = int(input("Invalid column: "))

    r_choice = int(input("Enter the row number."))-1

    while not(0 <= r_choice <= 4 and 0 <= c_choice <= 4):
        print("Invalid choice")
        c_choice = int(input("Enter the column number.")) - 1
        r_choice = int(input("Enter the row number.")) - 1
    while board[r_choice][c_choice] != 0:
        print("Already occupied place")
        c_choice = int(input("Enter the column number.")) - 1
        r_choice = int(input("Enter the row number.")) - 1'''

    board = add_piece(board, c_choice, player)
    draw(board)

    won = winner_check(board, player)

print("\nPlayer " + str(player) + " has won!")
