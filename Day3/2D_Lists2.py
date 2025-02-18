# Now if we want to create a 2D list from Scratch:

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]


# This prints each and every element in oour list i.e first we go into the list and we print each and every element of that list
for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()