# Concession stand program.
# It is sort of a menu.
# dictionary {key:value}

menu = {"pizzza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0


print("----------MENU--------")
#Here key, value is returned from menu.items(): eta 10=10 spaces
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------------")

while True:
    food = input("Select an item (q to quit) : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:  #if user writes food is not in our menu then it returns NONE
        cart.append(food)
        
print("---------Your order-------------")       
for food in cart:
    total += menu.get(food)  #menu.get(food) le chai afno value return garcha fno key ko
    print(food, end=" ")
    
print()
print(f"Total is: ${total:.2f}")

print(menu.get("nachos"))