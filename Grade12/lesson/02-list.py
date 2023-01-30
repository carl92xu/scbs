def isEmpty(q):
    return (len(q) == 0)


def isFull(q):
    return (len(q)==maxSize)


def search(q, item):
    '''print("Searching in:", q)
    print("Searching for:", item)
    found = False
    for i in range(len(q)):
        if q[i] == item:
            found = True
            break
    return found'''
    # easier way
    print("Search", item, "in", q)
    for i in range(len(q)):
        found = q[i] == item
        if found: break
    return found


def my_insert(q, item):
    # det if isFull, if yes exit
    # find index where to insert new item
    # move all items behind the index one pos right
    # insert the item at the pos of the index
    index = 0
    if isFull(q) is True:
        print("The list is full")
    else:
        for i in range(len(q)):
            if q[i] > item:
                index = i
                break
        # move all item behind the index 1 pos to the right
        q.append("")
        for j in range(len(q)-2, index, -1):
            q[j+1] = q[j]
        # insert item
        q[index] = item
    # OR
    # insert the item at the end
    # and then sort the array


def my_del(q, item):
    # del the item
    # move all item after it to the left
    pass


maxSize = 15
a = [1, 2, 3, 4, 5, 6, 7, 8, 10, 1, 2, 1, 1]

print(a)

# count(item)
print(a.count(1))
print(a.count(0))

# removes the first occurance of an item
a.remove(1)
print(a)

# return the index of first appearance
print(a.index(1))

# insert(pos, item)
a.insert(0, 1000)
print(a)

# pop() remove and return the last item of the list
print(a.pop())
print(a)

# pop(pos)
print(a.pop(1))
print(a)

print(isEmpty(a))
print(isFull(a))

# search(list, item)
print(search(a, 11))
print(search(a, 1))

my_insert(a, 9)
print(a)
