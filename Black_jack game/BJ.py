import tkinter as tk
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J', 'A']
suits = ['♥️', '♦️', '♣️', '♠️']
full_deck = [(card, suit) for card in deck for suit in suits]
random.shuffle(full_deck)

player_hand = []
dealer_hand = []
dealer_turn = False

def dealcard(turn):
    card = random.choice(full_deck)
    turn.append(card)
    full_deck.remove(card)

def total(turn):
    total = 0
    face = ['K', 'Q', 'J']
    aces = 0
    for card in turn:
        card_value = card[0]
        if isinstance(card_value, int):
            total += card_value
        elif card_value in face:
            total += 10
        elif card_value == 'A':
            aces += 1
    for _ in range(aces):
        total += 11 if total + 11 <= 21 else 1
    return total

def hit():
    dealcard(player_hand)
    update_display()
    if total(player_hand) > 21:
        result_label.config(text="You Bust! Dealer Wins.")
        disable_buttons()

def stand():
    global dealer_turn
    dealer_turn = True
    while total(dealer_hand) < 17:
        dealcard(dealer_hand)
    update_display()
    determine_winner()
    disable_buttons()

def determine_winner():
    player_total = total(player_hand)
    dealer_total = total(dealer_hand)
    if dealer_total > 21:
        result_label.config(text="Dealer Busts! You Win!")
    elif player_total > dealer_total:
        result_label.config(text="You Win!")
    elif player_total < dealer_total:
        result_label.config(text="Dealer Wins!")
    else:
        result_label.config(text="It's a Tie!")

def update_display():
    player_label.config(text=f"Player Hand: {player_hand} (Total: {total(player_hand)})")
    if dealer_turn:
        dealer_label.config(text=f"Dealer Hand: {dealer_hand} (Total: {total(dealer_hand)})")
    else:
        dealer_label.config(text=f"Dealer Hand: {dealer_hand[:1]} & [??]")

def disable_buttons():
    hit_button.config(state=tk.DISABLED)
    stand_button.config(state=tk.DISABLED)

def reset_game():
    global player_hand, dealer_hand, full_deck, dealer_turn
    dealer_turn = False
    full_deck = [(card, suit) for card in deck for suit in suits]
    random.shuffle(full_deck)
    player_hand = []
    dealer_hand = []
    dealcard(player_hand)
    dealcard(player_hand)
    dealcard(dealer_hand)
    dealcard(dealer_hand)
    update_display()
    result_label.config(text="")
    hit_button.config(state=tk.NORMAL)
    stand_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Blackjack Game")

player_label = tk.Label(root, text="Player Hand: ")
dealer_label = tk.Label(root, text="Dealer Hand: ")
result_label = tk.Label(root, text="", font=("Arial", 14))
player_label.pack()
dealer_label.pack()
result_label.pack()

hit_button = tk.Button(root, text="Hit", command=hit)
stand_button = tk.Button(root, text="Stand", command=stand)
reset_button = tk.Button(root, text="New Game", command=reset_game)

hit_button.pack()
stand_button.pack()
reset_button.pack()

reset_game()
root.mainloop()
