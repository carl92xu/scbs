def bubble_sort(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


'''test code
a = [20, -5, 3, -2, 17, 1, 6]
bubble_sort(a)
print(a)'''
