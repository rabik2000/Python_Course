# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if 18 <= age < 100:
    print("You can enter the club")
elif age < 0:
    print("You are still in the womb")
elif age >=100:
    print("Shut your face grandpa")
else:
    print("Get out of the bar")