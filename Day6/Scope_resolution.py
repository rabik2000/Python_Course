# variable_scope = where a variable is visible and accessible
# scope resolution = (LEGB) rule = Local -> Enclosed -> Global -> Built-in

# Variable_Scope:
# We cannot do this as this will result in an error
# Functions cannot see inside of other functions

# 1) Local Scope:
# def func1():
#     a = 1
#     print(a)
    
# def func2():
#     b = 2
#     print(b)
    
# func1()
# func2()


# 2) Enclosed Scope:
# def func1():
#     x = 1
#     def func2():
        
#         print(x)
#     func2()
    
# func1()  # Yo case ma 1 print garcha as there is no local so enclosed takes priority

# 3) Global Scope:
# x = 5
# def func1():
#      print(x)
    
# def func2():
#      print(x)

# func1()

# 4) Built-In Scope:

from math import e
def func1():
    print(e)

func1()