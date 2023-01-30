itemNumber = []
itemDescription = []
reservePrice = []
NumberOFBids = []

for i in range(2):
    itemNumInput = input("Please enter the item Number")
    itemNumber.append(itemNumInput)
    itemDescInput = input("Please enter the des")
    itemDescription.append(itemDescInput)
    reservePriceInput = int(input("Please enter the reversePrice"))
    while reservePriceInput < 0:
        reservePriceInput = int(input())
    reservePrice.append(reservePriceInput)
    NumberOFBids.append(0)

for i in range(len(itemNumber)):
    print("Item Number:", itemNumber[i])
    print("Item Description:", itemDescription[i])
    print("Reserve Price:", reservePrice[i])
    print("Number of Bids:", NumberOFBids[i])
