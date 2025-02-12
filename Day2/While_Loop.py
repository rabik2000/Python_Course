# while loop = execute some code WHILE some condition remains TRUE

name = input("Enter your name: ")

#if you dont have a good exit stategy you will end up in an infinite loop
while name == "":
    print("You did not write your name")
    name = input("Enter your name: ")

print(f"Hello {name}")