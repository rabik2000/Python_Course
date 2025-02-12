# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")


if len(username) > 12:
    print("Your name cannot be more than 12 charcters")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")
# yo case ma chai isalpha matra vako vaye run hunthyo = True vako vaye run hunthyo tara "not" cha  which means that the elif ststament runs if it is false
#vanepachi isaplpha digit cha vane false aucha ani not vanekai false line ho yo condition ma run huncha
elif not username.isalpha():
    print("your username cannot contain any digits")
else:
    print(f"Welcome {username}")
    
