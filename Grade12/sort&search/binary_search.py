import bubble_sort as bs


# return sorted list and target index
def binary_search(a, tar):
    # bubble sort the list
    bs.bubble_sort(a)

    front = 0
    rear = len(a)
    found = False
    while found is False:
        mid_index = round((rear-front+1) / 2)
        if tar < a[mid_index]:
            front = 0
            rear = mid_index - 1
        elif tar > a[mid_index]:
            front = mid_index+1
            rear = len(a)
        else:
            return a, mid_index

    return a, found


'''test code
a = [400, 312, 255, 1, -5, 155, 10, 100]
print(binary_search(a, 100))'''
