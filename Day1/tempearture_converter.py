
unit = input("What is your unit of measurement? (C or F)?: ")
temp = float(input("What is your temperature value? : "))

if unit == "C":
    temp = round(temp * (9/5) + 32,2)
    unit = "F"
elif unit == "F":
    temp = round((temp - 32) * (5/9),2)
    unit = "C"
else:
    print("Hawa kura nagara ")
    
print(f"The temperature is {temp} {unit} ")