def change_element(a_list, index, new_element):
    a_list[index] = new_element


def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n


grade = ["A", "B", "A", "C", "A", "D"]
print(grade)
print(count(grade, "A"))
change_element(grade, 2, "C")
print(grade)
