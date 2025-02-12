#Exercise 3:

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter a food you like (q to quit): ")
    
# print("bye")

# Exercise 4:

num = int(input("Enter a number between 1 and 10: "))

while num <1 or num > 10:
     print(f"Enter a valid number as {num} is not valid")
     num = int(input("Enter a number between 1 and 10: "))