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
    while reservePriceInput < 0:
        reservePriceInput = input()
    reservePrice.append(reservePriceInput)
    bidNumber.append(0)'''

# test code
for i in range(1, 4):
    itemNumber.append(str(i))
    itemDescription.append(chr(i+65))
    reservePrice.append(int(i + 100))
    bidNumber.append(0)

# display info
for i in range(len(itemNumber)):
    print("\nItem Number:", itemNumber[i])
    print("Item Description:", itemDescription[i])
    print("Reserve Price:", reservePrice[i])
    print("Number of Bids:", bidNumber[i])

# initialising lists
bidBuyerIDSeq = []
# bidItemNumSeq = []
bidPriceSeq = []
for i in range(len(itemNumber)):
    bidBuyerIDSeq.append(str(0))
    # bidItemNumSeq.append(str(0))
    bidPriceSeq.append(0)

# test
# bidBuyerIDSeq = ['1', '2', '0']
# bidItemNumSeq = ['1', '2', '0']
# bidPriceSeq = [101, 101, 0]
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
            if bidPriceSeq[count] < reservePrice[count]:
                bidOrNot = input("Bid or Not(y/n): ")
                if bidOrNot == "y":
                    bidNumber[count] += 1
                    bidPrice = int(input("The Price You Want To Bid: "))
                    if bidPrice > bidPriceSeq[count]:
                        bidPriceSeq[count] = bidPrice
                        bidBuyerIDSeq[count] = buyerNumber
                        # bidItemNumSeq[count] = itemNumChosen
                        print("\nbidBuyerIDSeq:", bidBuyerIDSeq)
                        print("itemNumber:", itemNumber)
                        print("bidPriceSeq:  ", bidPriceSeq)
                    else:
                        print("Your Price is Lower Than the Highest Bid")
                    break
            else:
                print("The Item Has Already Reached Reserve Price")
                break
        count += 1
    if itemFound is False:
        print("Item Number Not Found")
    buyerNumber = input("\nEnter Your Buyer Number: ")

# end of auction
soldCount = 0
didntReachCount = 0
noBidCount = 0
for i in range(len(itemNumber)):
    if int(bidPriceSeq[i]) >= int(reservePrice[i]):
        print("\nSold:")
        print("Item Number:", itemNumber[i])
        print("Buyer:", bidBuyerIDSeq[i])
        print("Final Price Sold:", round(float(bidPriceSeq[i]) * 1.1, 1))
        soldCount += 1
    elif int(bidPriceSeq[i]) <= int(reservePrice[i]) and int(bidPriceSeq[i]) != int(0):
        print("\nDidn't Reach Reserve Price:")
        print("Item Number:", itemNumber[i])
        print("Final Bid:", float(bidPriceSeq[i]))
        didntReachCount += 1
    elif int(bidPriceSeq[i]) == int(0):
        print("\nThis Item Has No Bid")
        print("Item Number:", itemNumber[i])
        noBidCount += 1

print("\nNumber of Sold:", soldCount)
print("Number of Didn't Reach:", didntReachCount)
print("Number of No Bid:", noBidCount)
print("\nExit")
