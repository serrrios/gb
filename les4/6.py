from itertools import count
from itertools import cycle

for el in count(int(input('Введите стартовое число (цикл закончиться на 15) :'))):
    if el > 15:
        break
    else:
        print(el)

con = 0
my_list = [True, 'ABC', 123, None]
print("Цикл будет повторяться до 10ого элемента: ")
for el in cycle(my_list):
    if con > 8:
        break
    print(el)
    con += 1