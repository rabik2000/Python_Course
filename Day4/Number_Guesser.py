# Python Number Guessing game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print("Python Number Guessing game")
print(f"Select a number between {lowest_num} and {highest_num}: ")

while is_running:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        print(f"Guesses: {guesses}")
        
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Select a number between {lowest_num} and {highest_num}: ") 
        elif guess < answer:
            print("Your guess is lower than the answer")
        elif guess > answer:
            print("Your guess is higher than the answer")
        else:
            print(f"Correct Guess, Bravo!!!!, the answer is {answer}")
            is_running = False
        
    else:
        print("invalid guess")
        print(f"Select a number between {lowest_num} and {highest_num}: ") 
        
print(f"The total amounts of guesses you had: {guesses}")

