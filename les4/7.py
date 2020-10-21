from itertools import count
from math import factorial

def func_gen():
    for el in count(1):
        yield factorial(el)

generator = func_gen()
x = 0
for i in generator:
    if x < 15:
        print(i)
        x += 1
    else:
        break