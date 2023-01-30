def count_char_in_str(a, b):
    n = 0
    for item in a:
        if item == b:
            n += 1
    return n


def count(a, b):
    n = 0
    for item in a:
        if item == b:
            n += 1
    return n


def first_appear(a, b):
    for i in range(len(a)):
        if a[i] == b:
            return i
