# blackjack_game.py
import random

# Constants
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        value += values[card[0]]
        if card[0] == 'A':
            ace_count += 1
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

def display_hand(name, hand, hide_first=False):
    if hide_first:
        print(f"{name}'s Hand: [Hidden], {hand[1][0]} of {hand[1][1]}")
    else:
        cards = ', '.join([f"{r} of {s}" for r, s in hand])
        print(f"{name}'s Hand: {cards} (Total: {calculate_hand_value(hand)})")

def player_turn(deck, hand):
    while True:
        display_hand("Player", hand)
        choice = input("Do you want to [H]it or [S]tay? ").lower()
        if choice == 'h':
            hand.append(deck.pop())
            if calculate_hand_value(hand) > 21:
                display_hand("Player", hand)
                print("You BUST!\n")
                return False
        elif choice == 's':
            print("You chose to STAY.\n")
            return True
        else:
            print("Invalid input. Enter 'H' or 'S'.")

def dealer_turn(deck, hand):
    while calculate_hand_value(hand) < 16:
        hand.append(deck.pop())
    display_hand("Dealer", hand)
    if calculate_hand_value(hand) > 21:
        print("Dealer BUSTS!\n")
        return False
    return True

def check_winner(player_hand, dealer_hand):
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    if player_total > 21:
        return "Dealer wins!"
    elif dealer_total > 21:
        return "Player wins!"
    elif player_total > dealer_total:
        return "Player wins!"
    elif player_total < dealer_total:
        return "Dealer wins!"
    else:
        return "It's a tie!"

def play_game():
    player_wins = 0
    dealer_wins = 0

    while True:
        print("\n=== NEW ROUND ===")
        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        display_hand("Dealer", dealer_hand, hide_first=True)

        player_in_game = player_turn(deck, player_hand)

        if player_in_game:
            dealer_in_game = dealer_turn(deck, dealer_hand)
        else:
            dealer_in_game = True
            display_hand("Dealer", dealer_hand)

        result = check_winner(player_hand, dealer_hand)
        print(result)

        if "Player wins" in result:
            player_wins += 1
        elif "Dealer wins" in result:
            dealer_wins += 1

        print(f"Score -> Player: {player_wins} | Dealer: {dealer_wins}")

        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()