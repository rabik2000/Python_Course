# Keyword_Arbitrary_Arguments  <class 'dict'>
# **kwargs  = allows you to pass multiple keyword-arguments
#             * =  unpacking operator
#           1. positional  2.default  3. keyword  4. ARBITRARY

def print_address(**kwargs):
    # print(type(kwargs))  # O/P:<class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="Albequrque 123", city= "New-Mexico City", state="New-Mexico", zip="1234356")