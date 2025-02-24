#List_Comprehension for strings

#Upper case banako for fruits
# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]

# print(fruits)

#Now take the first letter and put it in a new list
fruits = ["apple", "orange", "banana", "coconut"]
fruit_char = [fruit[0] for fruit in fruits]
print(fruit_char)


#Now, lets work with numbers:
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num > 0]
negative_nums = [num for num in numbers if num <0]
even_nums = [num for num in numbers if num % 2 == 0]
even_nums = [num for num in numbers if num % 2 != 0]
print(even_nums)


#Exercise:
#Grades:

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)