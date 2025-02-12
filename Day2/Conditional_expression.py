#Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

num = 10

#agadi ko print garcha if condition staisfy garyo vane ani else chai last ko print garcha
#print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"
print(result)

a= 5
b =6
max_num = a if a > b else b
min_num = a if a < b else b

print(max_num)
print(min_num)

temp = 10
weather = "Hot" if temp > 20 else "Cold"
print(weather)
