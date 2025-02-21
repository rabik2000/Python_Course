# default arguments = A default value for certain parameters
#                     default is used when certain parameters is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3.keyword, 4. arbitrary

def net_price(List_price, discount = 0, tax = 0.05):
    return List_price * (1 - discount) * (1 + tax)

# print(net_price(500))

print(net_price(500, 0.1))

print(net_price(500, 0.1, 0))