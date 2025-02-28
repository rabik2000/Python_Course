# Multiple Inheritance = inherit from more than one parent class
#                        C(A,B)

# class Prey:
#     def flee(self):
#         print("this animal is running away")

# class Predator:
#     def hunt(self):
#         print("this animal is hunting")

# class rabbit(Prey):
#     pass

# class hawk(Predator):
#     pass

# class fish(Prey, Predator):
#     pass

# rabbit = rabbit()
# hawk = hawk()
# fish = fish()

# print(rabbit.hunt())    #O/P: AttributeError: 'rabbit' object has no attribute 'hunt'
# fish.flee()
# fish.hunt()




# Multi level inheritance = inherit from a parent which inherits from another parent
#                           C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"this {self.name} is eating")
class Prey(Animal):
    def flee(self):
        print("this animal is running away")

class Predator(Animal):
    def hunt(self):
        print("this animal is hunting")

class rabbit(Prey):
    pass

class hawk(Predator):
    pass

class fish(Prey, Predator):
    pass

rabbit = rabbit("rabbit")
# hawk = hawk()  #ini haru ko lai pani naam pass garnu parcha
# fish = fish()

rabbit.eat()  # esle chai aba prey bata animal to inherit garcha