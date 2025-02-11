#Logical operators =  evaluate multiple conditions (or, and , not)
#                  or = atleast one condition must be True
#                  and = both conditions must be True
#                  not = inverts the condition (not False, not True) True cha vane false banaidincha and False cha vane True banaidincha

temp = 28
is_raining = False

# yo case ma is_raining vaneko true ma set Huncha
# Or case
if temp > 35 or temp <0 or is_raining:
    print("The event is cancelled")
else:
    print("The event is on")
    
#And case
is_sunny = False
if temp >= 28 and is_sunny:
    print("it is hot outside and sunny")
elif temp <=0 and is_sunny:
    print("It is cold outside and sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm and sunny") 

#Not case
if temp>=28 and not is_sunny:
    print("Warm and not sunny")    