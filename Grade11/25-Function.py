def count(a, b):
    n = 0
    for item in a:
        if item == b:
            n += 1
    return n


def count_char_in_str(a, b):
    n = 0
    for item in a:
        if item == b:
            n += 1
    return n


def first_appear(a, b):
    for i in range(len(a)):
        if a[i] == b:
            return i


myList = [1, 2, 3, 4, 3, 2, 2]
print(count(myList, 2))

myStr = "aaaaaaaaaasjkfdlhihlakjlkaa"
print(count_char_in_str(myStr, "a"))

print(first_appear(myStr, "j"))

print(ord("B"))
print(chr(65))

state = "Florida"
print(state.count("B"))
print(state.find("r"))
print(state.upper())
print(state.lower())
print(dir("abc"))
