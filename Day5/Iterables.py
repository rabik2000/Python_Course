# Iterables = An object/collection that can return its element one at a time,
#             allowing it to be iterated over in a loop

# 1) LIST:
# numbers = [1, 2, 3, 4, 5]

# for number in reversed(numbers):
#     print(number)
    
# 2) TUPLE:
# numbers = (1, 2, 3, 4, 5)

# for number in numbers:
#     print(number)
    
# 3) SETS: they are not reversible
# fruits = {"apple", "orange", "banana", "coconut"}

# for fruit in reversed(fruits):
#     print(fruit)
    
# 4) Dictionary:
# 1) This only prints the keys
# my_dictionary = {"A": 1,
#                  "B": 2,
#                  "C": 3}
# for key in my_dictionary:
#     print(key)

# 2) This only prints the values as the iterables
# my_dictionary = {"A": 1,
#                  "B": 2,
#                  "C": 3}

# for  value in my_dictionary.values():
#     print(value)
    
# 3) This prints both the values and the keys
my_dictionary = {"A": 1,
                 "B": 2,
                 "C": 3}

for key, value in my_dictionary.items():
    print(f"{key}: {value}")