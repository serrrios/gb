number = int(input("Enter number: "))
my_list = [7, 4, 3, 2]
i = 0
for element in my_list:
    if number <= element:
        i+=1
my_list.insert(i, number)
print(my_list)