def linear_search(a, tar):
    for i in range(len(a)):
        if a[i] == tar:
            return i
    return False


a = [5, 7, 13, 18, 1000, -5]
index = linear_search(a, 1000)
print(index)
