from OOP_car import Car   # this is done so as to keep our file clean
        
car1 = Car("Mustang", "2024", "Red", False)
# print(car1)   #When we print here we are given the memory address of the object

# Now to access the object within the class
print(car1.model)

car2 = Car("Corvette", "2025", "green", True)
print(car2.color)

car1.drive()   #used as a method
car2.stop()    #used as a method