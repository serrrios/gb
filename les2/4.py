inp = input("Enter str: ").split()
count = 1
for i in inp:
    print (f"{count}: {i[:10]}")
    count += 1
