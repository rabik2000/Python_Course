# Count-up timer using default arguments

import time

def count(end, start = 0):  #Default Arguments jaiale last ma huncha
    for x in range(start, end+1):  # becuase in range the end is exclusive
        print(x)
        time.sleep(1)
    print("DONE")
    
# count(10)  #start from 0 to 10

count(20, 15)  #starts from 15 to 20
