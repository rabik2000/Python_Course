# Keyword_Argument = an argument preceded by an identifier
#                    helps with readability
#                    order of arguments doesn't matter
#                    1. Positional      2. default      3. KEYWORD      4. arbitrary



def hello(greeting, title, first, last):
    print(f"{greeting}  {title} {first} {last}")
    
hello("Hello", last = "Spongy", first = "Babery", title = "Blue")  #jasko aba positional argument specify gareko huncha usko chai first ma huna parcha
#aba yo hello lai last ma lekheko vae syntax error aucha

#print from 1 to 10
# for x in range(1, 11):
#     print(x, end= " ")   # here end is also a keyword_argument
    
# print("1", "2", "3", sep = "-")  #here sep is also a keyword_argument

