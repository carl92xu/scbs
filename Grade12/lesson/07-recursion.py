def factorial(n):  # may contain bugs
    while n > 997:
        try:
            n = int(input("Please input a number smaller than or equal to 997: "))
        except:
            pass
    if n == 0:
        f = 1
    else:
        f = n * factorial(n-1)
    return f


def calcsum(n):
    if n > 0:
        n += calcsum(n-1)
    return n


def evensum(n):
    if n > 0:
        n += evensum(n-2)
    return n


def addnum_rec(n):
    if len(n) > 1:
        n[0] += addnum_rec(n[1:])
    print(n[0])
    return n[0]


def addnum_for(n):
    s = 0
    for i in range(len(n)):
        s += n[i]
    return s


def fib(n):
    if n < 3:
        s = n - 1
    else:
        s = fib(n-1) + fib(n-2)
    return s


def binary_search_rec(search_list, search_item, front, rear):
    middle = (front + rear) // 2
    if search_list[middle] < search_item:
        binary_search_rec(search_list, search_item, middle+1, rear)
    elif search_list[middle] > search_item:
        binary_search_rec(search_list, search_item, front, middle-1)
    else:  # correct this part
        print("Found at position:", middle)
        pass


name_list = ["Ann", "Boyd", "Cyrus", "Dylan", "Mia", "Nathan", "Sam"]
name_list_front = 0
name_list_rear = len(name_list) - 1
binary_search_rec(name_list, "Mia", name_list_front, name_list_rear)
