# Python weight converter program

weight = float(input("Enter your weight: "))
unit = input("Kg or lbs? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"
else:
    print("Lastai moto raichau ki K ra L lekha vaneko arkai dekhera arkai lekhechau")

print(f"Your weight is {round(weight,2)} {unit}")