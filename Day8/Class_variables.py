# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class


class Student:
    
    class_year = 2022  #good_practice to access this through class rather than object
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        
student1 = Student("rabik", 12)
student2 = Student("rabikk", 16)
student3 = Student("asda", 12)

print(student2.name)
print(student2.age)
# print(student2.class_year)  this way we dont know tyo attribute object ko ho ki class ko vanera
#the pratice is:
print(Student.class_year)
print(Student.num_students)  #prints no of students