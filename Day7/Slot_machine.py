# Python Slot Machine Program
import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]  # This is a List
    result = []
    for symbol in range(3):
        result.append(random.choice(symbols))
    return result
    # Alternatively, we can use list comprehension:
    #List Comrehension:
    # return [random.choice(symbols) for _ in range(3)]  # _ =everything for range 3
    
def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍋':
            return bet * 7
        elif row[0] == '🔔':
            return bet * 9
        elif row[0] == '⭐':
            return bet * 11
    return 0

def main():
    balance = 100
    print("***********************************")
    print("Welcome to Python Slots Machine")
    print("Symbols: 🍒 🍉  🍋 🔔 ⭐ ")
    print("***********************************")
    
    
    while balance > 0:
        print(f"Current Balance: ${balance}")
        
        bet = input("Place your bet amount: ")
        
        if not bet.isdigit():
            print("Please enter a valid number")
            continue  # skips the current iteration and moves to next iteration
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient balance")
            continue
        
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        
        balance -= bet
        
        row = spin_row()   # this will be a List
        print("Spinning...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("good Luck Next time")
            
        balance += payout
        
        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.upper() != 'Y':
            break
    print("***********************************")    
    print(f"Game Over! Your final balance is ${balance}")
    print("***********************************")
if __name__ == '__main__':
    main()