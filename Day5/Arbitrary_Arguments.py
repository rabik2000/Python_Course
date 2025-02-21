# Arbitrary Arguments:
# *args    = allows you to pass multiple non-key arguments  = "tuple" form
# **kwargs  = allows you to pass multiple keyword-arguments  = "dictionary" form
#             * =  unpacking operator
#           1. positional  2.default  3. keyword  4. ARBITRARY


#aba yo 1,2 ra 3 pass garyo vane chaldaina ni ta tesaile hamilai arbitrary arguments chaieko ho
# def add(a, b):
#     return a + b

# print(add(1,2))

#also parameter name args may vary, it can be nums or whatever you like
# def add(*args):    #when we do this it takes variable no of arguments in a "tuple" form
#     total = 0
#     for arg in args:
#         total += arg
#     return total
        

# total = add(1, 2, 3, 4)
# print(total)


#Function to display someone's name:

def display_name(*args):
    for arg in args:
        print(arg, end= " ")
        
display_name("Dr.", "Sheldon", "Cooper")