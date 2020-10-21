def my_func(**args):
    return ' '.join(args.values())
print(my_func(name = 'Sergey', surname = 'Krasnov',  year = '1991', city = 'Krasnoyasrk', email = 'test@test.ru', phone = '88002000600'))
