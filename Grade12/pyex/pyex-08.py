def find(board, choice):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if choice == board[i][j]:
                return i, j


def show(board):
    for array in board:
        print(array)


def init(row, col):
    board = []
    chr_count = 0
    for r in range(row):
        board.append([])
        for c in range(col):
            board[r].append(chr(chr_count+97))
            if chr_count == 1:
                board[r][c] = BLANK
            chr_count += 1
    return board


row_size = 1
col_size = 4
BLANK = " "
# grid = [["a", BLANK, "c", "d"], ["e", "f", "g", "h"], ["i", "j", "k", "l"], ["m", "n", "o", "p"]]
grid = init(row_size, col_size)

while True:
    show(grid)

    # choice input
    choice = input("\nEnter a choice: ").lower()
    choice_valid = False
    while choice_valid is False:
        if len(choice) == 1 and 96 < ord(choice) < (96+row_size*col_size) or choice in ["save", "load", "exit"]:
            choice_valid = True
        else:
            choice = input("Please re-enter choice, the choice is invalid: ").lower()

    if choice == "save":
        file = open("game.txt", "w")
        file.write(str(len(grid))+"\n")  # number of rows
        file.write(str(len(grid[0]))+"\n")  # number of columns
        for i in range(len(grid)):  # save each element in a line
            for j in range(len(grid[i])):
                file.write(str(grid[i][j])+"\n")
        file.close()
        break  # exit program after saving
    elif choice == "load":
        file = open("game.txt", "r")
        count = 0
        for line in file:
            line = line.strip("\n")
            # print(line)
            if count == 0:
                row_num = int(line)
            elif count == 1:
                col_num = int(line)
            else:  # load element into grid
                i = (count-2) // 4
                j = (count-2) % 4
                grid[i][j] = line
            count += 1
        file.close()
    elif choice == "exit":
        break
    else:
        # letter check
        while (choice not in grid[0]) and (choice not in grid[1]) and (choice not in grid[2]) and (choice not in grid[3]):
            choice = input("Please re-enter choice, the letter is invalid: ").lower()

        row, column = find(grid, choice)
        # print("Position: ("+str(row) + "," + str(column)+")")

        try:
            while grid[row-2][column] != BLANK and grid[row][column-2] != BLANK and grid[row+2][column] != BLANK \
                    and grid[row][column+2] != BLANK:  # Test Needed!!!
                choice = input("Please re-enter choice, the letter can't be moved: ").lower()
                row, column = find(grid, choice)
                # print("Position: (" + str(row) + "," + str(column) + ")")
        except:
            pass

        # direction input
        direction = input("Enter a direction (u, d, l, r): ").lower()
        while direction not in ["u", "d", "l", "r"]:
            direction = input("Please re-enter direction: ").lower()

        # main logic
        if direction == "r" and column+2 < len(grid[0]) and grid[row][column+2] == BLANK and grid[row][column+1] != BLANK:
            grid[row][column] = BLANK
            grid[row][column+1] = BLANK
            grid[row][column+2] = choice
        elif direction == "l" and column-2 >= 0 and grid[row][column-2] == BLANK and grid[row][column-1] != BLANK:
            grid[row][column] = BLANK
            grid[row][column-1] = BLANK
            grid[row][column-2] = choice
        elif direction == "u" and row-2 >= 0 and grid[row-2][column] == BLANK and grid[row-1][column] != BLANK:
            grid[row][column] = BLANK
            grid[row-1][column] = BLANK
            grid[row-2][column] = choice
        elif direction == "d" and row+2 < len(grid) and grid[row+2][column] == BLANK and grid[row+1][column] != BLANK:
            grid[row][column] = BLANK
            grid[row+1][column] = BLANK
            grid[row+2][column] = choice
        else:
            print("Invalid move")

    # remaining piece count
    piece_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != BLANK:
                piece_count += 1
    print("Piece left:", piece_count, "\n")
    if piece_count == 1:
        print("You won!")
        break
print("\nExit")
