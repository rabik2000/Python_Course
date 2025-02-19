# Function to input and display an invoice

# def display_invoice(username, amount, due_date):
#     print(f"Hello, {username}")
#     print(f"Your bill is: ${amount} and due until: {due_date}")
    
# display_invoice("Rabik", 4100, "01/02/25")
    
# return in a function
# return  = statement used to end a function
#           and send a result back to the caller

# def add(x, y):
#     return(x+y)

# z = add(1, 2)

# print(z)
# print(add(1, 2))


#Function to create a full name
def create_name(first, last):
    first = first.capitalize() #first letter capitalize gareko
    last = last.capitalize()    #first letter capitalize gareko
    return first + " " + last

print(create_name("rabik", "thapa"))