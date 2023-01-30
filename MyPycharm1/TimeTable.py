Monday=['Math','Politics','English','Chinese','IT','Physics','IT','IT']
Tuesday=['IT','Math','English','Chemistry','Physics','Physics','IT','IT']
Wednesday=['Math','English','Chemistry','Chemistry','IT','IT','Politics','Chinese']
Thursday=['English','Math','IT','IT','Shooting','Shooting','Go','Go']
Friday=['Math','English','Physics','Physics','Chemistry','Chemistry','English','Math']

a = input('Which day?')
b = int(input('Which class?'))

if a == 'Monday':
    print(Monday[b - 1])
elif a == 'Tuesday':
    print(Tuesday[b - 1])
elif a == 'Wednesday':
    print(Wednesday[b - 1])
elif a == 'Thursday':
    print(Thursday[b - 1])
elif a == 'Friday':
    print(Friday[b - 1])
elif a == 'monday':
    print(Monday[b - 1])
elif a == 'tuesday':
    print(Tuesday[b - 1])
elif a == 'wednesday':
    print(Wednesday[b - 1])
elif a == 'thursday':
    print(Thursday[b - 1])
elif a == 'friday':
    print(Friday[b - 1])

print('Have a good day!')