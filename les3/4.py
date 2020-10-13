def my_func(x, y):
    res = 1
    yy = abs(y)
    while yy > 0:
        res = res * (1 / x)
        yy-=1
    return res
print(my_func(int(input("Chislo 1: ")),int(input("Chislo 2: "))))