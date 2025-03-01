import random
import time
player_In = True
dealer_in = True
game_in = True
# deck of cards / player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J', 'A']
suits = ['♥️', '♦️', '♣️', '♠️'] 
full_deck = [(card, suit) for card in deck for suit in suits]
random.shuffle(full_deck)

player_hand = []
dealer_hand = []

# deal the cards
def dealcard(turn):
    card = random.choice(full_deck)
    turn.append(card)
    full_deck.remove(card)

    

# calculate the total of each hand
def total(turn):
    total = 0
    face = ['K', 'Q', 'J']
    for card in turn:
        card_value = card[0]  # Get the card value from the tuple (card value, suit)
        if isinstance(card_value, int) and card_value in range(1, 11):   #checks if card value is integer type
            total += card_value
        elif card_value in face:
            total += 10  # Face cards are worth 10 in Blackjack, not 1
        elif card_value == 'A':
            if total > 11:
                total += 1
            else:
                total += 11
    return total
        


# check for winner
def revealDealerHand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]

#display hand
def display_hand(turn):
    print(f"You have {turn} for a total of {total(turn)}")   
#display dealer hand
def dealer_display(turn):
    print(f"Dealer has {turn} for a total of {total(turn)}")

# game loop
for _ in range(2):
    dealcard(dealer_hand)
    dealcard(player_hand)
print(f"Dealer has {revealDealerHand()} and  XX")
print("\n")
print(f"You have {player_hand} for a total of {total(player_hand)}")
if total(player_hand) == total(dealer_hand):
    print("Dealer and Player both has Natural Black Jack")
    print(f"Dealer Hand: {dealer_hand} with a total of : {total(dealer_hand)}")
    game_in = False
elif total(player_hand) == 21:
    print("You have a Natural Blackack")
    game_in = False
elif total(dealer_hand) == 21:
    print("The dealer has a Natural Blackjack, You Lose!")
    display_hand(dealer_hand)
    game_in = False
else:
    while player_In or dealer_in:
        while player_In:
                stayOrHit = input("Here are your Options(Select 1 or 2): \n 1. Stay    2. Hit: ")
                if stayOrHit == '1':
                    player_In = False
                else:
                    dealcard(player_hand)
                    display_hand(player_hand)
                    if total(player_hand) > 21:
                        display_hand(player_hand)
                        print("You have Gone Bust")
                        player_In = False
                        dealer_in =  False
                        game_in = False
                    if total(player_hand) == 21:
                        display_hand(player_hand)
                        print("Blackjack for You")
                        player_In = False
                    
        while dealer_in:
            if total(dealer_hand) > 16:
                print("Final Result: \n")
                dealer_display(dealer_hand)
                dealer_in = False
            else:
                dealcard(dealer_hand)
                dealer_display(dealer_hand)
                if total(dealer_hand) > 21:
                    print("You Win, Dealer Bust")
                    dealer_in = False
                    game_in =  False
                if total(dealer_hand) == 21:
                    print("Dealer has Blackjack")
                    dealer_hand = False
                time.sleep(1)
 
while game_in:               
    if total(dealer_hand) > total(player_hand):
        print("Dealer Wins")
    elif total(dealer_hand) < total(player_hand):
        print("Player Wins")
    else:
        print("PUSH")       
    game_in = False
            
            
    
    
