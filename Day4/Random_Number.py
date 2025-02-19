import random

# print(help(random))

#this makes a random integer
# number = random.randint(1, 6)  # esma 6 pani inclusive huncha

#Now for a random float
# number = random.random()

#This is a random choice for a rock-paper scissor game
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

#now a card game
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
#Now i can shuffle them
random.shuffle(cards)
print(cards)