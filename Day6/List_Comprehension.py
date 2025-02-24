# List comprehension = A concise(brief but comprehensive) way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

#This is a traditional for loop
#We here print the values of doubles
# doubles = []
# for x in range(1,11):
#     doubles.append(x*2)
    
# print(doubles)

#List_Comprehsnsion

# doubles = [expression for value in iterable]
doubles = [x*2 for x in range(1,11)]  # here 11 is exclusive as range ko last is exclusive
print(doubles)