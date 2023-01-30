'''
DECLARE num, hundreds, tens, units: INTEGER
INPUT num
hundreds <- num DIV 100
            345 DIV 100 = 3
tens <- (num MOD 100) DIV 10
        (345 MOD 100) = 45
        45 DIV 10 = 4
units <- (num MOD 100) MOD 10
        (345 MOD 100) = 45
        45 MOD 10 = 5
OUTPUT "Hundreds:", hundreds, "Tens:", tens, "Units:", units
'''
