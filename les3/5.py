def my_func():
    res = 0
    while True:
        string = input("Vvedite stroku cifr, stop symbol 'Q': ").split()
        for tmp in string:
            if tmp.isdigit():
                res = res + int(tmp)
            elif tmp == "Q":
                return res
print(my_func())