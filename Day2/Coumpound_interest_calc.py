# Python Compund Interest calculator

principle = float(input("enter principle: "))

while principle <= 0:
    print("principle can't be less than or equal to 0")
    principle = float(input("enter principle: "))
    
rate = float(input("enter rate: "))

while rate <= 0:
    print("rate can't be less than or equal to 0")
    rate = float(input("enter rate: "))
    
time = float(input("enter time: "))

while time <= 0:
    print("time can't be less than or equal to 0")
    time = float(input("enter time: "))
    
total = principle * pow((1 + rate/100), time)
print(f"Your total interest is : {total:.2f}")
