import random

def card_total(cards):
    user_cards = 0
    aces = 0

    for card in cards:
        if card in ['J', 'K', 'Q']:
            user_cards += 10 
        elif card == 'A':
            user_cards += 11
            aces += 1
        else:
            user_cards += int(card)  
        
    while user_cards > 21 and aces > 0:
        user_cards -= 10
        aces -= 1
        
    return user_cards

def create_deck():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = values * 4
    random.shuffle(deck)
    return deck

def main():
    print("=== BLACKJACK ===\n")
    
    # Gets the users bet
    bet = int(input("Enter your bet: $"))
    
    # Create deck and deal
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    # Show initial hands of both user and dealer
    print(f"\nYour cards: {player_hand} (Total: {card_total(player_hand)})")
    print(f"Dealer shows: [{dealer_hand[0]}, ?]\n")
    
    # Player turn
    doubled = False
    while card_total(player_hand) < 21:
        # Can only double on first turn (2 cards)
        if len(player_hand) == 2:
            choice = input("(H)it, (S)tand, or (D)ouble? ").upper()
        else:
            choice = input("(H)it or (S)tand? ").upper()
        
        if choice == 'H':
            player_hand.append(deck.pop())
            print(f"You drew: {player_hand[-1]}")
            print(f"Your hand: {player_hand} (Total: {card_total(player_hand)})\n")
        elif choice == 'D' and len(player_hand) == 2:
            bet *= 2  # Double the bet if user wants to double (D)
            player_hand.append(deck.pop())
            doubled = True
            print(f"DOUBLED! Bet is now ${bet}")
            print(f"You drew: {player_hand[-1]}")
            print(f"Your hand: {player_hand} (Total: {card_total(player_hand)})\n")
            break  # Turn ends after double (Only works on 1 hand, forces game end after)
        elif choice == 'S':
            break
    
    player_total = card_total(player_hand)
    
    # Check if player busted
    if player_total > 21:
        print(f"BUST! You lose ${bet}\n")
    else:
        # Dealers turn
        print(f"Dealer reveals: {dealer_hand} (Total: {card_total(dealer_hand)})")
        
        while card_total(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
            print(f"Dealer draws: {dealer_hand[-1]} (Total: {card_total(dealer_hand)})")
        
        dealer_total = card_total(dealer_hand)
        
        print(f"\n=== FINAL ===")
        print(f"You: {player_total} | Dealer: {dealer_total}")
        print(f"Bet: ${bet}\n")
        
        if dealer_total > 21:
            print(f"Dealer busts! YOU WIN ${bet}! ")
        elif player_total > dealer_total:
            print(f"YOU WIN ${bet}! ")
        elif player_total < dealer_total:
            print(f"Dealer wins. You lose ${bet} ")
        else:
            print("PUSH (tie) - Bet returned")
    

    again = input("\nPlay again? (Y/N): ").upper()
    if again == 'Y':
        main()


main()









