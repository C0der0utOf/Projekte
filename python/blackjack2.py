import random

# Constants
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
}

# Classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        total = sum(values[card.rank] for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'Ace')
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

# Game logic
def play_blackjack(player_money):
    print("\n=== New Round ===")
    print(f"Current balance: ${player_money}")

    # Get the player's bet
    while True:
        try:
            bet = int(input("Place your bet: $"))
            if bet > player_money or bet <= 0:
                print("Invalid bet amount.")
            else:
                break
        except ValueError:
            print("Enter a valid number.")

    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    for _ in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    print("\nYour hand:", player_hand)
    print("Dealer shows:", dealer_hand.cards[0])

    # Player turn
    while True:
        print("Your hand value:", player_hand.value())
        if player_hand.value() > 21:
            print("You busted!")
            return player_money - bet
        move = input("Hit or Stand? (h/s): ").lower()
        if move == 'h':
            player_hand.add_card(deck.deal())
            print("You drew:", player_hand.cards[-1])
        elif move == 's':
            break
        else:
            print("Invalid input.")

    # Dealer turn
    print("\nDealer's hand:", dealer_hand)
    while dealer_hand.value() < 17:
        card = deck.deal()
        dealer_hand.add_card(card)
        print("Dealer draws:", card)

    print("Dealer's final hand:", dealer_hand)
    print("Your value:", player_hand.value(), "Dealer value:", dealer_hand.value())

    # Outcome
    player_total = player_hand.value()
    dealer_total = dealer_hand.value()

    if dealer_total > 21 or player_total > dealer_total:
        print("You win!")
        player_money += bet
    elif dealer_total > player_total:
        print("Dealer wins!")
        player_money -= bet
    else:
        print("It's a tie! Your bet is returned.")

    return player_money

# Main loop
if __name__ == "__main__":
    balance = 100  # Starting money

    while balance > 0:
        balance = play_blackjack(balance)
        print(f"Your balance is now: ${balance}")
        if balance <= 0:
            print("You're out of money! Game over.")
            break
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break
