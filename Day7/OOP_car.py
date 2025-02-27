# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
# You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):      #Constructor
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    # Methods: methods are actions that our attributes can perform
     
    def drive(self):
         print(f"You drive the {self.model}")
    
    def stop(self):
        print(f"you stop the {self.model}")     