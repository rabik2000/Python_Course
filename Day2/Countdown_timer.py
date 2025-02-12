import time
#sleeps for a set amt oftime
#time.sleep(5)

my_time = int(input("Enter the time in seconds: "))

#this will increment from 0 to my time 
# for x in range(0, my_time):
#     print(x)
#     time.sleep(1)
    
#But if you want it in reverse. -1 here decrements our value
# for x in range(my_time, 0, -1):
#     print(x)
#     time.sleep(1)

#Now if you want to calculate time
for x in range(my_time, 0, -1):
     seconds = x % 60
     minutes = int(x/60) % 60
     hour = int(x/3600)
     print(f"{hour:02}:{minutes:02}:{seconds:02}")
     time.sleep(1)

print("Time")