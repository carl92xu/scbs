#functions

#?????
def last_person_to_borrow(a): #this finds the name of the last person to borrow a particular book
    borrowers = []
    file = open("txtfile/loans.txt","r")
    for line in file:
        words = line.split(":")
        if words[0] == a:
            borrowers.append(words[1])
    if len(borrowers) == 0:
        return("Nobody")
    else:
        return(borrowers[-1])
    file.close

#->
def menu(): #places the menu on the screen
    file = open("txtfile/books.txt","r")
    print("\n**********************************")
    print("** CODE   TITLE")
    for line in file:
        words = line.split(":")
        print ("** "+ words[0]+"    "+words[1])
    print("**")
    print("**    type EXIT to end the program")
    print("**    type TOTAL to count loans of a particular book")
    print("**    type STATS to count all Loans")
    print("**    type LAST to find last person to boorow a particular book")
    print("**")
    print("**********************************")
    file.close()

#->
def number_of_time_loaned(a): #this returns the numeber of times a book is loaned given its code.
    file = open("txtfile/loans.txt","r")
    count = 0
    for line in file:
        words = line.split(":")
        if words[0] == a:
            count = count + 1
    return(count)
    file.close()

######
def book_loans(): #this returns the numeber of times all books have been loaned.
    bookcode = []
    file = open("txtfile/books.txt","r")
    for line in file:
        words = line.split(":")
        bookcode.append(words[0])
    file.close()

    for i in range(0,len(bookcode)):
        file = open("txtfile/loans.txt", "r")
        count = 0
        for line in file:
            words = line.split(":")
            if words[0]== bookcode[i]:
                count = count +1
        print("Book ",find_book_title(bookcode[i])," was borrowed ",count,"times")
        file.close()

#->
def find_book_title(a):  #returns the title of a book given the code
    file = open("txtfile/books.txt","r")
    for line in file:
        words = line.split(":")
        if words[0] == a:
            title = words[1]
    return(title)
    file.close()

#->
def quit(): #places the menu on the screen
    print("*************")
    print("**         **")
    print("** GOODBYE **")
    print("**         **")
    print("*************")

#####
def save_loan_details(a,b):   #saves the loan details give the code and name
    file = open("txtfile/loans.txt","a")
    file.write(a+":"+b+"\n")
    file.close()
    print("Thank you that record has been added")


## Code starts here
menu()
print ("Which book is being borrowed?")
bookID = input("--->")

while bookID != 'EXIT':
    if bookID == 'TOTAL':
        print ("Which book do you wish to count?")
        bookID = input("--->")
        print(find_book_title(bookID)," was borrowed ", number_of_time_loaned(bookID),"times")
    elif bookID == 'STATS':
        book_loans()
    elif bookID == 'LAST':
        print ("Which book do you want to find the last borrower?")
        bookID = input ("--->")
        print("the last person to borrow ",find_book_title(bookID), "was ", last_person_to_borrow(bookID))
    else:
        print ("Who is borrowing",find_book_title(bookID),"?")
        name = input("--->")
        save_loan_details(bookID,name)

    menu()
    print("Which book is being borrowed?")
    bookID = input("--->")
quit()