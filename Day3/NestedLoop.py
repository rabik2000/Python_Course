# Nested Loop = A loop within another loop (outer, inner)
#                Outer Loop:
#                       Inner Loop:

#it will print 1-9 3 times 
for x in range(3):
    for y in range(1, 10):
        print(y, end = "")
    print()