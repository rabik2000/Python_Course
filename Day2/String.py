
#name = input("Enter your full name: ")

#len prints the length of the string
#print(len(name))

#finds the character in the string, gives it position in the string
#result = name.find("R")

#finds the character in the string in reverse i.e last occurence
#result = name.rfind("a")

#Make everything capital letters
#result = name.capitalize()

#make everything uppercase
#result = name.upper()

#make everything lowercase
#result = name.lower()

#To check whether the string is all digit or not, gives output in terms of bool values-True or False
#result = name.isdigit()


#To check whether the string is all alphabets or not, gives output in terms of bool values-True or False
#result = name.isalpha()

#print(result)

phone_number = input("Enter your phone number: ")

#prints the count of "-" contained in a string
#result = phone_number.count("-")

#replacement of a character 
result = phone_number.replace("-", "")


print(result)
