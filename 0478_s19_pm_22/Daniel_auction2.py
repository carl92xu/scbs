# Daniel Sun
# 12-March
# Auction-pre-release 2019
# --------------------------------------------
# DECLARE numOfItems : INTEGER
# numOfBids <-----10
numOfItems = 2
# Declare item number: array [1: number of items] OF INTEGER
itemNumber = []
# Declare description: array [1: number of items] OF INTEGER
description = []
# Declare reserve Price: array [1: number of items] OF Real
reservePrice = []
# Declare number of Bids: array [1: number of items] OF INTEGER
numOfBids = []

for index in range(numOfItems):
    itemNumber.append(index+1)
    print("Input item #", itemNumber[index], " description:", sep='', end='')
    description.append(input())
    print("Input item # ", index+1, " reserve price:", sep='', end='')
    reservePrice.append(float(input()))
    numOfBids.append(0)

print(itemNumber)
print(description)
print(numOfBids)
print(reservePrice)

# DECLARE highestBid: ARRAY [1: numOfItems] OF REAL
highestBid = []
# DECLARE highestBidBuyer: ARRAY [1: numOfItems] OF REAL
highestBidBuyer = []

for k in range(numOfItems):
    highestBid.append(0)
    highestBidBuyer.append(None)
while True:
    for j in range(numOfItems):
        print(itemNumber[j], description[j], highestBid[j], numOfBids[j])

    print("\nDo you want to make entry for bidding? Y/N:", end='')
    # DECLARE choice: CHAR
    choice = input()
    if choice == "y" or choice == "Y":
        # DECLARE buyerNum: INTEGER
        buyerNum = int(input("Please input your buyer number:"))
        # DECLARE buyerBid: INTEGER
        buyerBid = int(input("Please input itemNumber to bid for an item:"))
        numOfBids[buyerBid - 1] = numOfBids[buyerBid - 1] + 1
        print("Please input your price for bidding:", end='')
        # DECLARE bidPrice: REAL
        bidPrice = float(input())

        if bidPrice >= highestBid[buyerBid - 1]:
            highestBid[buyerBid - 1] = bidPrice
            if highestBid[buyerBid - 1] >= reservePrice[buyerBid -1]:
                highestBidBuyer[buyerBid - 1] = buyerNum
    if choice == 'n' or choice == 'N':
        break

print(highestBid)    
print(highestBidBuyer)



         
        
           
        
        
        
        
        




