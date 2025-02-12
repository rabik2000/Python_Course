# Format Specifiers = {:flags} format a value based on what flags are inserted
# Format Specifiers are used in the context of an f-string e.g: print(f"text")

# :.(number)f = round to that many decimal places (fixed point)
# print(f"Price 1 is ${price1:.3f}")
# print(f"Price 2 is ${price2:.3f}")
# print(f"Price 3 is ${price3:.3f}")

# :(number) = allocate that many spaces
# print(f"Price 1 is ${price1:10}")
# print(f"Price 2 is ${price2:10}")
# print(f"Price 3 is ${price3:10}")

# :03 = allocate and zero pad that many spaces
# print(f"Price 1 is ${price1:09}")
# print(f"Price 2 is ${price2:09}")
# print(f"Price 3 is ${price3:09}")

# :< = left justify
# print(f"Price 1 is ${price1:<9}")
# print(f"Price 2 is ${price2:<9}")
# print(f"Price 3 is ${price3:<9}")

# :> = right justify
# print(f"Price 1 is ${price1:>9}")
# print(f"Price 2 is ${price2:>9}")
# print(f"Price 3 is ${price3:>9}")

# :^ = center align
# print(f"Price 1 is ${price1:^9}")
# print(f"Price 2 is ${price2:^9}")
# print(f"Price 3 is ${price3:^9}")

# :+ = use a pulse sign to indicate positive value
# print(f"Price 1 is ${price1:+}")
# print(f"Price 2 is ${price2:+}")
# print(f"Price 3 is ${price3:+}")

# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 332323.14159
price2 = -9872323.65
price3 = 1223.34

#Now to indicate higher numbers with comma and only 2 decimal ponts
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")

