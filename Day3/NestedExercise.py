#Print a retangle of a symbol that we have set

rows  = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use to print a rectangle: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()