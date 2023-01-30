itemNumber = []
itemDescription = []
reservePrice = []
bidNumber = []

# record info
'''for i in range(2):
    itemNumInput = input("itemNumInput")
    itemNumber.append(itemNumInput)
    itemDescInput = input("itemDescInput")
    itemDescription.append(itemDescInput)
    # How to do validation...
    reservePriceInput = input("reservePriceInput")
    while reservePrice < 0:
        reservePriceInput = input()
    reservePrice.append(reservePriceInput)
    bidNumber.append(0)'''

# test code
for i in range(3):
    itemNumber.append(str(i))
    itemDescription.append(chr(i+65))
    reservePrice.append(str(i + 100))
    bidNumber.append(0)

# display info
for i in range(len(itemNumber)):
    print("\nItem Number:", itemNumber[i])
    print("Item Description:", itemDescription[i])
    print("Reserve Price:", reservePrice[i])
    print("Number of Bids:", bidNumber[i])

# initialising lists
bidBuyerIDSeq = []
bidItemNumSeq = []
bidPriceSeq = []
for i in range(len(itemNumber)):
    bidBuyerIDSeq.append(str(0))
    bidItemNumSeq.append(str(0))
    bidPriceSeq.append(0)
print("\nbidBuyerIDSeq", bidBuyerIDSeq)
print("bidItemNumSeq", bidItemNumSeq)
print("bidPriceSeq  ", bidPriceSeq)

# record bids
buyerNumber = input("\nEnter Your Buyer Number: ")
# validation
while buyerNumber != 0:
    itemNumChosen = input("Choose an item number: ")
    # validation?
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
                    bidItemNumSeq[count] = itemNumChosen
                    print("\nbidBuyerIDSeq", bidBuyerIDSeq)
                    print("bidItemNumSeq", bidItemNumSeq)
                    print("bidPriceSeq  ", bidPriceSeq)
                else:
                    print("Your Price is Lower Than the Highest Bid")
                break
        count += 1
    if itemFound is False:
        print("Item Number Not Found")
    buyerNumber = input("\nEnter Your Buyer Number: ")
    # validation

print("Exit")
