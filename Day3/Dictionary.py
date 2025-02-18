# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates.

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow",
            "Nepal": "Kathmandu",
            "Bhutan": "Thimpu",
            "Thailand": "Bangkok"}

# as thailandw is not on the list the output returns NONE
# print(capitals.get("Thailandw"))

#This is how we check the data from the dictionary by using .get
# if capitals.get("Thailand"):
#     print("that capital exists")
# else:
#     print("No")


# #Lets update our dictionary
# capitals.update({"Germany": "Berlin"})

# #Lets change the values within the dictionary or replace them
# capitals.update({"India": "Bihar"})

# # To remove a key-value pair, we can use the POP Method using Key:
# capitals.pop("Bhutan")


# #Now if we want to remove the last item then :
# capitals.popitem()

#Now to clear the dictionary:
# capitals.clear()
# print(capitals)

#Now to only print the keys: in this context country name
# keys = capitals.keys()
# print(keys)


# This is OOP so we can use it in a FOR Loop
# for key in capitals.keys():
#     print(key)
    
    
#Now to only get the values:
# values = capitals.values()
# print(values)

# #Now to print Values using a for Loop:
# for value in capitals.values():
#     print(value)

#This is Tricky: This is the Items method:
# this prints both the keys and the values:
# items = capitals.items()
# print(items)

# Now the same .items can also be used in a FOR Loop:
for key, value in capitals.items():
    print(f"{key}: {value}")