# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)  #just lika a child inheriting attributes from a paent

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating ")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
        
class Dog(Animal):  #Inheritance gareko even tho yo dog empty cha 
    pass

class cat(Animal):   # khali navaye pani afnai pani huna sakcha
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("mew")

dog = Dog("Scooby")
cat = cat("gato")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)  #Esari inherit garako

mouse.eat()
mouse.sleep()   #esari vitra ko objects pani access garna milcha

mouse.speak()