# exercise 2 shopping cart program

item = input("What item would you like to buy? ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like? "))

Total = price * quantity
print(f"You have bought {price} x {quantity} \n")
print(f"Your total is: ${Total}")