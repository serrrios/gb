list = []
num = int(input("Enter number of elements : "))
for i in range(0, num):
    tmp = int(input(f"Enter element {i+1}: "))
    list.append(tmp)
print(f"Result: {list}")
i = 0
while i < (num - 1):
    list[i], list[i+1] = list[i+1], list[i]
    i += 2
print(f"Result after manipulate: {list}")