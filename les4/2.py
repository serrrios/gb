my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Исходный список: {my_list}")
new_list = [el for i, el in enumerate(my_list) if my_list[i - 1] < my_list[i] and i != 0]
print(f"Новый список: {new_list}")