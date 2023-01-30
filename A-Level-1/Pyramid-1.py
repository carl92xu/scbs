space = ' '

def InputMaxSymbolNum():
    MaxSymbolNum = input("Please input max symbol number")
    while int(MaxSymbolNum) % 2 == 0:
        MaxSymbolNum = input("Please input max symbol number")
    return(MaxSymbolNum)

def SetValue():
    symbol = input("Please input symbol")
    MaxSymbols = InputMaxSymbolNum()
    spaces = (int(MaxSymbols)-1)/2
    symbols = 1
    return(symbol,MaxSymbols,spaces,symbols)

def AdjustValue(spaces,symbols):
    spaces = spaces - 1
    symbols = symbols + 2
    return(spaces,symbols)

symbol,MaxSymbols,spaces,symbols = SetValue()

while int(symbols) <= int(MaxSymbols):
    print(str(int(spaces)*space)+str(int(symbols)*symbol))
    spaces,symbols = AdjustValue(spaces,symbols)