from script1 import *
# aba yo mthi ko run garda pani sabbai print handincha
# Program from Script 1:
# def favorite_food(food):
#     print(f"Your favorite food is: {food}")


# print("This is Script1")
# favorite_food("pizza")
# print("Bye")
#Output:
# This is Script1
# Your favorite food is: pizza
# Bye

def favorite_drink(drink):
    print(f"Your favoritedrink is {drink}")
    
def main():
    print("This is Script2")
    favorite_food("sushi") #only to run a function from script 1 as we are importing it from script1
    favorite_drink("pepsi")
    print("uj")

if __name__ == '__main__':  # we are adding this so it can run as a standalone program
    main()