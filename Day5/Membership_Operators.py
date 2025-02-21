# Membership operators = used to test whether a value or a variable is found in a sequence
#                        (string, list, tuple, set or dictionary)
#                         1. in
#                         2. not in
#                         we can also use "and" "or" to add to ins and 2 not ins i.e. if '@' in email and '.' in email:

# 1.STRING:

# A. In:
# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter.capitalize() in word:
#     print(f"There is a {letter}")
# else:
#     print("nope")
    
#B. Not in:
# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter.capitalize() not in word:
#     print("nope")
# else:
#     print(f"There is a {letter}")
    
    
# 2. SET:
 
# students = { "spongebob", "patrick", "sandy"}

# student = input("Enter the name of a student: ")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} is not a student")
    
# 3. Dictionary:

grades = {"sandy": "A",
          "squidward": "B",
          "spongebob": "C",
          "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")  # here {grades[student]} is done so as to find out the value of a student grades in a dictionary without using any commands
else:
    print(f"{student} is not found")