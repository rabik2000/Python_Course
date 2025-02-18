# Collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK.
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates.
# Tuple = () ordered and unchangeable. Duplicates OK. Faster.

fruit = ["Apple", "orange", "Banana"]
# #It selects the range
# print(fruit[0:2])

# #Now to print it backwards
# print(fruit[::-1])

# #We can also iterate over them over a For loop

# for x in fruit:
#     print(x)

# It prints all the activities that we can do with the Collection
# print(dir(fruit))


#Wee can also use the help functiion if needed
# print(help(fruit))

#Now to return the length of the my collection list
# print(len(fruit))

#Now to return a bool value True or False to say whether a fruit is in my collection or not
# print("Apple" in fruit)

#Now to change the value in my List
# fruit[0] = "Pineapple"
# print(fruit)

#Now we can also append into the List( AT the end)
# fruit.append("Mango")
# print(fruit)

# #Now to remove an item from the list
# fruit.remove("orange")
# print(fruit)

#Now we can also insert a value at a certain point in the Index without deletion just moves the outstanding value to the next value
# fruit.insert(0, "Grapes")
# fruit.insert(3,"peach")
# fruit.insert(11, "Kiwi")   #Yo case ma chai 11 haley vane siddai last ma gayera basyo


# #Now to sort them in an alphabetical order
# fruit.sort()
# print(fruit)

#Now to reverset the list
# fruit.reverse()


#Now to clear all the values from a list
# fruit.clear()


#Now to return the index of a value

# print(fruit.index("Banana"))

#Now to count the duplicate values in the index
print(fruit.count("Banana"))