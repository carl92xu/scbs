import random


def printRules():
    print("The computer will think of either rock, paper or scissors.")
    print("You will enter r for Rock, p for Paper ot s for Scissors.")
    print("The computer will reveal it's choice and the winner.")
    print()


def playGame():
    choice = input("Enter r for rock, p for paper or s for scissors: ").lower()
    while choice not in ["r", "p", "s"]:
        choice = input("Please re-enter, r for rock, p for paper or s for scissors: ").lower()
    computerChoice = random.randint(0, 2)  # 0=rock, 1=paper, 2=scissors
    if computerChoice == 0:
        print("The computer chose: Rock")
    elif computerChoice == 1:
        print("The computer chose: Paper")
    else:
        print("The computer chose: Scissors")

    if choice == "r":
        if computerChoice == 0:
            print("It's a draw")
        elif computerChoice == 1:
            print("Computer Wins")
        else:
            print("Player Wins")
    elif choice == "s":
        if computerChoice == 2:
            print("It's a draw")
        elif computerChoice == 0:
            print("Computer Wins")
        else:
            print("Player Wins")
    else:
        if computerChoice == 1:
            print("It's a draw")
        elif computerChoice == 2:
            print("Computer Wins")
        else:
            print("Player Wins")


print("Welcome to the Rock, Paper, Scissors Game")
print("========================================")
printRules()
play = True
while play is True:
    playGame()
    asked = input("\nDo you want to play again or not, enter y/n: ")
    if asked == "n":
        play = False
print("Exit")
