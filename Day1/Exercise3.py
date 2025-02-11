# Exercise 3: Calculate the circumference and area of a circle

import math

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius

#We have used the round here to round the numbers after decimal upto 2 digits
print(f"The circumference is: {round(circumference,2)}cm")

#area = math.pi * (radius ** 2)
#alternatively this can also be done using pow built in command
area = math.pi * pow(radius,2)
print(f"The area of the circle is: {round(area,2)}cm²")