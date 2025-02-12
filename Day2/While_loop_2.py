
age = int(input("enter your age: "))

while age < 0:
    print("Enter a valid age!")
    age = int(input("enter your age: "))
    
print(f"your age is {age}")