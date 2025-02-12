# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.
# here last range 11 is exclusive i.e not included
#here reversed goes from 10 to 1

for x in reversed(range(1, 11)):
    print(x)
print("Happy new year")

#here 2 is the gap it takes
for x in range(1, 11, 2):
    print(x)
    
#here we can also use for for strings    
cred_card = "1234-1233-1233-3424"

for x in cred_card:
    print(x)