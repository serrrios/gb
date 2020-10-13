my_dict = {1 : 'winter', 2 : 'winter', 3 : 'spring', 4: 'spring', 5: 'spring', 6 : 'summer', 7 : 'summer', 8 : 'summer', 9 : 'autumn', 10 : 'autumn', 11 : 'autumn', 12 : 'winter'}
my_list = list(my_dict.values())
mesyac = int(input(f"Enter number month: "))
if mesyac > 0 and mesyac < 13:
    print(f"It's {my_list[mesyac-1]}")
    print(f"It's {my_dict.get(mesyac)}")
else:
    print("Number month bad")