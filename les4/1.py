from sys import argv

def my_funk(time, price, prem):
    return(time * price) + prem

print(my_funk(int(argv[1]), int(argv[2]), int(argv[3])))