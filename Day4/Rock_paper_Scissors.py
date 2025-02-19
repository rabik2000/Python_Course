# Rock, paper, Scissors game

import random

options = ("rock", "paper", "scissors")
running = True

while running:
    
    player = None
    computer = random.choice(options)
    
    #This means that the user will have to keeep on entering until the user enters the correct data
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    else:
        print("You Lose!")
        
    play_again = input("Play Again? (Y/N): ").lower()
    if not play_again == "y":  # this means that if play again is different from y running is set to false which stops the program
        running = False
        
print("thanks for playing")