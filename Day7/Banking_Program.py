# Python banking Program

# if we want to make a program, we divide them into smaller sections:
import math

#  1. Show Balance
# First we define a function to show balance:

def show_balance(balance):
    floored_balance = math.floor(balance)
    print("******************************")
    print(f"Your balance is ${floored_balance}.{int((balance - floored_balance) * 100):02d}")
    print("******************************")


# 2. Deposit
def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    
    if amount <=0:
        print("******************************")
        print("That's not a valid amount!")
        print("******************************")
        return 0
    else:
        return amount

# 3. Withdraw

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))
    
    if amount > balance:
        print("******************************")
        print("Insufficient funds! ")
        print("******************************")
        return 0
    elif amount <=0:
        print("******************************")
        print("Invalid Amount ")
        print("******************************")
        return 0
    else:
        return amount
 
# Defining Variables:
# now to encapsulate this all in an int_main function:

def main():
    balance = 0
    is_running = True

    while is_running:
        print("******************************")
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("******************************")
        choice = input("Enter your choice (1-4): ")
        
        match choice:
            case '1':
                show_balance(balance)
            case '2':
                balance += deposit()
            case '3':
                balance -= withdraw(balance)
            case '4':
                is_running = False
            case _:
                print("Not a valid choice")
        
    print("Thank you for using our Service! ")
    print("******************************")
    
if __name__ == '__main__':
    main()