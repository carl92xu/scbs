def insertion_sort(a):
    for i in range(0, len(a)-1):
        element = a[i+1]
        while i >= 0 and element < a[i]:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = element


'''test code
mylist = [7, 5, 18, 3, 1000, -5]
insertion_sort(mylist)
print(mylist)
'''
