#Typecasting = the process of converting a variable from one data type to another
#              str(), int(), float(), bool()

name = ""
age = 25
gpa = 3.2
is_student = True

age +=1
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))

age = str(age)
age +="1"
print(age)
print(type(age))


name = bool(name)
print(name)