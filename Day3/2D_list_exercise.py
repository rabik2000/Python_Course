# here we create a 2D KeyPad

# 2D-tuple

num_pad = ((1, 2, 3),
           (4, 5, 5),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()
        