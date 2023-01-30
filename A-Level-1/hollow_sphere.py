space = ' '

def InputMaxSymbolNum():
    MaxSymbolNum = input("Please input max symbol number:")
    while int(MaxSymbolNum) % 2 == 0:
        MaxSymbolNum = input("Please input max symbol number:")
    return(MaxSymbolNum)

def SetValue():
    symbol = input("Please input symbol:")
    MaxSymbols = InputMaxSymbolNum()
    spaces = (int(MaxSymbols)-1)/2
    spaces2 = -1
    return(symbol,MaxSymbols,spaces,spaces2)

def AdjustValue(spaces,spaces2):
    spaces = spaces - 1
    spaces2 = spaces2 + 2
    return(spaces, spaces2)

def AdjustValue2(spaces,spaces2):
    spaces = spaces + 1
    spaces2 = spaces2 - 2
    return(spaces, spaces2)

symbol,MaxSymbols,spaces,spaces2 = SetValue()

print(str(int(spaces)*space)+str(symbol))

while spaces2 < (int(MaxSymbols)-3):
    spaces, spaces2 = AdjustValue(spaces, spaces2)
    print(int(spaces)*str(space) + str(symbol) + int(spaces2)*str(space) + str(symbol))

while spaces < (int(MaxSymbols)-4):
    print(int(spaces)*str(space) + str(symbol) + int(spaces2)*str(space) + str(symbol))
    spaces, spaces2 = AdjustValue2(spaces, spaces2)

print(str(int(spaces)*space)+str(symbol))