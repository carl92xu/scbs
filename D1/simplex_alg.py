def pretty_print(fn):
    print()
    for i in range(len(fn)):
        for j in range(len(fn[i])):
            print("{:<8}".format(round(fn[i][j], 2)), end="")
        print()


def var_print(fn):
    for i in range(len(fn)):
        print("{:<8}".format(fn[i]), end="")


def equ_print(equ_fn, var_fn):
    for i in range(len(equ_fn[0])):
        if i == 0:
            print(str(var_fn[i]), end="=")
        elif i == len(equ_fn[0]) - 1:
            print("="+str(equ_fn[0][i]))
        elif i == 1:
            print(str(round(equ_fn[0][i], 2)) + str(var_fn[i]), end="")
        else:
            if equ_fn[0][i] != 0:
                if equ_fn[0][i] > 0:
                    print("+"+str(round(equ_fn[0][i], 2))+str(var_fn[i]), end="")
                else:
                    print(str(round(equ_fn[0][i], 2)) + str(var_fn[i]), end="")
        '''else:
                if equ_fn[0][i] != 1 or -1 or 0:
                    if i == 1:
                        print(str(round(equ_fn[0][i], 2)) + str(var_fn[i]), end="")
                    else:
                        if equ_fn[0][i] > 0:
                            print("+" + str(round(equ_fn[0][i], 2)) + str(var_fn[i]), end="")
                        elif equ_fn[0][i] < 0:
                            print(str(round(equ_fn[0][i], 2)) + str(var_fn[i]), end="")
                elif equ_fn[0][i] == 1:
                    if i == 1:
                        print(str(var_fn[i]), end="")
                    else:
                        print("+" + str(var_fn[i]), end="")
                elif equ_fn[0][i] == -1:
                    if i == 1:
                        print("-" + str(var_fn[i]), end="")
                    else:
                        print("-" + str(var_fn[i]), end="")'''


def one_iteration(fn):
    for i in range(len(fn[0])):
        if fn[0][i] < 0:
            chosen_var = i
            break

    for i in range(len(fn)):
        try:
            if fn[i][-1] / fn[i][chosen_var] > 0:
                smallest = fn[i][-1] / fn[i][chosen_var]
                chosen_equ = i
                break
        except:
            pass
    for i in range(1, len(fn)):
        calc = fn[i][-1] / fn[i][chosen_var]
        if 0 < calc < smallest:
            smallest = calc
            chosen_equ = i
    print("\nsmallest:", smallest)
    print("chosen_equ:", chosen_equ)
    print("chosen_var:", chosen_var)

    temp = fn[chosen_equ][chosen_var]
    for i in range(len(fn[chosen_equ])):
        fn[chosen_equ][i] = fn[chosen_equ][i] / temp
    pretty_print(fn)

    for i in range(len(fn)):
        if i == chosen_equ:
            pass
        else:
            temp = -fn[i][chosen_var]
            for j in range(len(fn[i])):
                fn[i][j] = temp * fn[chosen_equ][j] + fn[i][j]
    pretty_print(fn)


var_list = ["P", "x", "y", "z", "r", "s", "RHS"]
my_fn = [[1, -5, -6, -4, 0, 0, 0],
          [0, 1, 2, 0, 1, 0, 6],
          [0, 5, 3, 3, 0, 1, 24]]

print("Original Equations:")
var_print(var_list)
pretty_print(my_fn)

all_positive = False
iteration_count = 0

while not all_positive:
    iteration_count += 1
    print("\n============================\nIteration", iteration_count)
    all_positive = True
    one_iteration(my_fn)
    for i in range(len(my_fn[0])):
        if my_fn[0][i] < 0:
            all_positive = False
            break

print("\n============================\nFinal Result:")
equ_print(my_fn, var_list)
