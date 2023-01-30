CoachCost <- 550
AnTicketCost <- 30
WHILE True THEN
    PRINT "Max Number of Student is 45"
    EstStudentNumber <-
    IF EstStudentNumber < 1 THEN
        PRINT "It should at least be 1"
    ELSEIF EstStudentNumber > 1 THEN
        PRINT "It should less than 45"
    ELSEIF EstStudentNumber IN 1 TO 45 THEN
        BREAK
    ENDIF
ENDWHILE
EstFreeTicketNumber <- INT(EstStudentNumber / 10)
EstTicketCost <- (EstStudentNumber - EstFreeTicketNumber) * AnTicketCost
EstTotalCost <- CoachCost + EstTicketCost
EstAveCost <- EstTotalCost / EstStudentNumber
PRINT "The cost of each student is", EstAveCost


Names <- []
Paid_Not <- []
Not <- []
Paid <- []
count <- 0
FOR i IN 1 TO EstStudentNumber
    INPUT StudentName
    Names <- StudentName
    PRINT "Paid or not(Input Y or N)"
    INPUT PaidOrNot
    Paid_Not <- PaidOrNot
NEXT
FOR item IN Paid_Not
    IF item == "N" THEN
        Not <- Names[count]
    ELSEIF item == "Y" THEN
        Paid <- Names[count]
    ENDIF
    count <- count + 1
NEXT
PRINT "Paid:",Paid
PRINT "Not Paid:",Not


WHILE True THEN
    PRINT "Max Number of Student is 45"
    StudentNumber <-
    IF StudentNumber < 1 THEN
        PRINT "It should at least be 1"
    ELSEIF StudentNumber > 1 THEN
        PRINT "It should less than 45"
    ELSEIF StudentNumber IN 1 TO 45 THEN
        BREAK
    ENDIF
ENDWHILE
FreeTicketNumber <- INT(StudentNumber / 10)
TicketCost <- (StudentNumber - FreeTicketNumber) * AnTicketCost
TotalCost <- CoachCost + TicketCost
AveCost <- TotalCost / StudentNumber
CollectedMoney <- LEN(Paid + 1) * AveCost
Final <- TotalCost - CollectedMoney