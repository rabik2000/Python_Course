# Shopping cart Program
# It is an exercise based on our previous study on Collectons. i.e. Set, Tuples and List.

foods = []
prices = []
total = []


while True:
    food = input("Enter a food to Buy: (Press q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("--------- YOUR CART ---------")

for food in foods:
    print(food, end = "         ")

print()

for price in prices:
    total += price
    
print(f"Your grand total is : ${total}")