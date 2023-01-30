BiggestSoFar = float(input("num1:"))
NextNum = float(input("num2:"))
if NextNum > BiggestSoFar:
    BiggestSoFar = NextNum
NextNum = float(input("num3:"))
if NextNum > BiggestSoFar:
    BiggestSoFar = NextNum
print(BiggestSoFar)