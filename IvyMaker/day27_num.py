largest = None
smallest = None
while True:
    inp = input('Enter a number:')
    try:
        inp = int(inp)
        if largest == None or inp > largest:
            largest = inp
        elif smallest == None or inp < smallest:
            smallest = inp
    except:
        if inp == 'done':
            break
        print('Invalid input')
print('Maximum is',largest)
print('Minimum is',smallest)