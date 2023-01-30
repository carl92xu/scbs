#Daniel
#12-March
#Acution-pnerelease 2019
#-----------------------------------------------------------------
#DECLARE ItemNumber:ARRAY[1:ItemNumber] OF INTEGER
ItemNumber = []

#DECLARE Description:ARRAY[1:Description] OF STRING
Description = []

#DECLARE ReservePrice:ARRAY[1:ReservePrice] OF REAL
ReservePrice = []

#DECLARE NumOfBids:ARRAY[1:NumOfBids] OF INTEGER
NumOfBids = []

for i in range(10):
    print("Please input the item number: ")
    number = input()
    ItemNumber.append(number)

    print("Please input the description: ")
    DescripeInput = input()
    Description.append(DescripeInput)

    print("Please input the reserve price: ")
    ReservePriceInput = input()
    NumOfBids.append(ReservePriceInput)

    print("Please input the number of bids: ")
    price = input()
    NumOfBids.append(price) 


