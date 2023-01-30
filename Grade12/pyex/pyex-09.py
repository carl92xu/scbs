import random


def getValue(card):
    try:
        return int(card)
    except:
        if card in ["J", "Q", "K"]:
            return 10
        else:
            return 11

def ace_recount(hand):
    score = 0
    for i in range(len(hand)):
        try:
            score += int(card)
        except:
            if card in ["J", "Q", "K"]:
                score += 10
            else:
                score += 1
    return score


print("Automatic Blackjack Player\n")
games = [0, 0, 0]
gameOver = False
deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"] * 500
random.shuffle(deck)
# print(deck, "\n")

while not gameOver:

    hand = []
    score = 0

    while score < 17 and len(deck) != 0:
        card = deck.pop()
        hand.append(card)
        score = score + getValue(card)
        if score > 21 and "A" in hand:
            score = ace_recount(hand)

    if score == 21:
        # print("Blackjack!")
        games[0] += 1
    elif score < 21:
        # print("You have scored " + str(score))
        games[1] += 1
    else:
        # print("Uh oh, you have gone bust!")
        games[2] += 1

    # print("Your cards were " + str(hand) + "\n")

    if len(deck) < 1:
        gameOver = True

# End of the game
number_of_game = sum(games)
print("\nYou played " + str(number_of_game) + " games.")
print("Blackjacks: "+str(round((games[0]/number_of_game)*100.0))+"%")
print("Games: "+str(round((games[1]/number_of_game)*100))+"%")
print("Busts: "+str(round((games[2]/number_of_game)*100))+"%")
