sum = 0
times = 0
avg = 0
while True:
    inp = input('Enter a number:')
    try:
        inp = int(inp)
        sum += inp
        times += 1
    except:
        if inp == 'done':
            break
        print('Invalid input')
avg = sum / times
print('sum is',sum)
print('times is',times)
print('avg is',avg)