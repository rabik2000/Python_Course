# Relates to OOP
# Output:
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# The above are attributes: a special variable
# print(dir())

# print(__name__)
# Output: __main__
# So that's why we can also see in programs that:
# if __name == '__main': #if name is equal to a string of main
#       main()       so as to call the function main

# from script2 import *  # * means everything
# print(__name__)

def favorite_food(food):
    print(f"Your favorite food is: {food}")

def main():
    print("This is Script1")
    favorite_food("pizza")
    print("Bye")


if __name__ == '__main__':
    main()

