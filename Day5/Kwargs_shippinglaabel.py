# Kwargs shipping label
#Using both args and kwargs in a program

def shipping_label(*args, **kwargs):   #if it was kwargs followed by args it would not function properly i.e. (**kwargs,*args) = syntax error
    for arg in args:
        print(arg, end = " ")
    print()
    
    #this will only print the values
    # for value in kwargs.values():
    #     print(value, end = " ")

    #Now to print the street in one line and city, state and zip in the other line
    if "apt" in kwargs:  #we are using the if statement because apt navayera ni print garaya vane output ma NONE vanera print huncha tesaile
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label("Dr.", "Spongebob", "Squarepants",
               street = "123 Fake Street",
               apt = "#100",
               city = "Detroit",
               state = "california",
               zip = "54321")