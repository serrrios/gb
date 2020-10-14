def int_func(arg):
    res = ''
    for i in arg.split():
        tmp_2 = i[0].upper()
        res = res + tmp_2 + i[1:]
        if i != arg.split()[-1]:
            res = res + ' '
    return res
print(int_func("testy test"))

#title()???
'''Why not this????:
def int_func(word):
    print(word.title())
int_func("testy test")
'''