itemNumber = []
itemDescription = []
reservePrice = []
bidNumber = []

# record info
for i in range(10):
    itemNumInput = input("itemNumInput: ")
    itemNumber.append(itemNumInput)
    itemDescInput = input("itemDescInput: ")
    itemDescription.append(itemDescInput)
    reservePriceInput = int(input("reservePriceInput: "))
    while reservePriceInput < 0:
        reservePriceInput = int(input("reservePriceInput again: "))
    reservePrice.append(reservePriceInput)
    bidNumber.append(0)
    print()

# display info
for i in range(len(itemNumber)):
    print("\nItem Number:", itemNumber[i])
    print("Item Description:", itemDescription[i])
    print("Reserve Price:", reservePrice[i])
    print("Number of Bids:", bidNumber[i])

# initialising lists
bidBuyerIDSeq = []
bidPriceSeq = []
for i in range(len(itemNumber)):
    bidBuyerIDSeq.append(str(0))
    bidPriceSeq.append(0)

print("\nbidBuyerIDSeq:", bidBuyerIDSeq)
print("itemNumber:", itemNumber)
print("bidPriceSeq:  ", bidPriceSeq)

# record bids
buyerNumber = input("\nEnter Your Buyer Number: ")
while str(buyerNumber) != str(0):
    itemNumChosen = input("Choose an item number: ")
    itemFound = False
    count = 0
    for item in itemNumber:
        if item == itemNumChosen:
            itemFound = True
            print("Number of Bids:", bidNumber[count])
            print("Reserve Price:", reservePrice[count])
            print("Item Description:", itemDescription[count])
            bidOrNot = input("Bid or Not(y/n): ")
            if bidOrNot == "y":
                bidNumber[count] += 1
                bidPrice = int(input("The Price You Want To Bid: "))
                if bidPrice > bidPriceSeq[count]:
                    bidPriceSeq[count] = bidPrice
                    bidBuyerIDSeq[count] = buyerNumber
                    print("\nbidBuyerIDSeq:", bidBuyerIDSeq)
                    print("itemNumber:", itemNumber)
                    print("bidPriceSeq:  ", bidPriceSeq)
                else:
                    print("Your Price is Lower Than the Highest Bid")
                break
        count += 1
    if itemFound is False:
        print("Item Number Not Found")
    buyerNumber = input("\nEnter Your Buyer Number: ")

print("Exit")
