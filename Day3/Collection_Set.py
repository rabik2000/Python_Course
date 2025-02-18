# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates.

fruits = {"apple", "orange", "banana", "coconut", "coconut"}

# print(fruits)

# to display all the different attributes and methods of a set
# print(dir(fruits))

# #for an in-depth study of these you can use the help command
# print(help(fruits))

# To print the length of a set
# print(len(fruits))

# To find whether the specific value is in a set or not =  returns bool value i.e. True or False
# print("apple" in fruits)

# We cannot  use: 
#                print(fruits[0])
#                                 because the set is not ordered so it cannot return this value.

# But we can add a value to a set
# fruits.add("pineapple")

# We can also remove a value from the set
# fruits.remove("apple")

# Now if we want to remove the first element from a set[remember that the popped element will be random]
# fruits.pop()

# Now if we want to clear the set then:
# fruits.clear()

fruits.add("apple")  # even though you have inserted a value to the set, it will not take any duplicate values
print(fruits)