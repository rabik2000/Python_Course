# Hangman in python
import random
from Words_for_Hangman import words


#Dictionary of key:() -> which is a tuple
hangaman_art = {0: ("   ",
                    "   ",
                    "   "),
                1: (" 0 ",
                    "   ",
                    "   "),
                2: (" 0 ",
                    " | ",
                    "   "),
                3: (" 0 ",
                    "/| ",
                    "   "),
                4: (" 0 ",
                    "/|\\",
                    "   "),
                5: (" 0 ",
                    "/|\\",
                    "/  "),
                6: (" 0 ",
                    "/|\\",
                    "/ \\")}



# for line in hangaman_art[6]:
#     print(line)


def display_man(wrong_guesses):
    print("*****************************")
    for line in hangaman_art[wrong_guesses]:
        print(line)
    print("*****************************")    

def display_hint(hint):
    print(" ".join(hint))   # bicha ma space haldya

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)  # random word select gariyo
    hint = ["_"] * len(answer)  #dash dash fill in the blank sapces jasto diyo
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():  #Checking only alphabet huna parcha vanera
            print("Invalid input")
            continue
        
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
            
        guessed_letters.add(guess)
        
        if guess in answer:        #Guess valid cha vane blank space ma answer halna
            for i in range(len(answer)):   #esma chai iterate gareko , if answer ko kunai letter match huncha vane hint ko tyo thau ma replace garaucha
                if answer[i] == guess:
                    hint[i] = guess    #blank space ma right guess halcha
        else:
            wrong_guesses += 1
            
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Win!")
            is_running = False
        elif wrong_guesses >= len(hangaman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lose!")
            is_running = False
    
if __name__ == '__main__':
    main()