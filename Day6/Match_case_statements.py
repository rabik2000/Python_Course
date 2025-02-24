# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                 Benefits: cleaner and syntax is more readable
# Syntax:  
#    match "case":
#          case "mathi ko case vako value":
#                 return value
        

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuessday"
#         case 4:
#             return "It is Wednesday"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _:  # Esko matlab kei pani nahuda
#             return "Not a Valid Day"
        
# print(day_of_week(6))


#Now we will check if it is weekend or not:
# aba dherai case repeat hune vayera we use or |
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:  # Esko matlab kei pani nahuda
            return "Not a Valid Day"
        
print(is_weekend("Monday"))