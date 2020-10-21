def first_func(var_1, var_2):
    if var_2 == 0:
        return "Bad param"
    else:
        return (var_1 / var_2)

pr1 = int(input("VVedite chislo 1: "))
pr2 = int(input("VVedite chislo 2: "))
print(first_func(pr1, pr2))


