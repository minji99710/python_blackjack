#blackjack game
import itertools
import random

def game_begin():
    #start : greet, make card deck, shuffle the card 
    greeting = 'Hello, welcome to bichon casino! Let me introduce your dealer today, kimbision.'
    print(greeting)
    username = input('What is your name, sir? : ')
    greeting_with_username = '\nNice to meet you {name}, it\'s a perfect day to gamble! \
    \nHave a good time with your puriti gambling bichon :)'.format(name=username)
    print(greeting_with_username)

    return username



def construct_card_deck():
    #add a card deck 
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['spades', 'clovers', 'diamonds', 'hearts']

    original_deck = list(itertools.product(suits, vals))
    return original_deck

def shuffle_card_deck(original_deck):
    shuffled_list = random.sample(original_deck, len(original_deck))
    print('\ncards are all shuffled! \n')

    return shuffled_list

def remove_burning_cards(shuffled_list):
    #remove the burning card 
    burning_card = []
    burning_card.extend([shuffled_list[0], shuffled_list[1]])
    del shuffled_list[0:2] 
    print('the burning cards have been removed ! It seems like we are all ready.\n')
    

def player_bet_money(username):
    #player bet money
    player_money = 100
    player_bet = input('How much would you bet, sir {name}? (you currently have $100): '.format(name=username))
    player_money -= int(player_bet)
    print('you have bet ${bet_money}, and now have ${player_money} left.'.format(bet_money=player_bet, player_money=player_money))
    player_state = ''

    return player_money, player_bet, player_state

#main game
scores = {'A':1, 'J':10, 'Q':10, 'K':10}
def calculate_hand(hand):
    hand_value = 0
    ace = False
    for card in hand:
        print(card)
        if card[1] == 'A':
            ace = True
        if card[1] in scores: 
            hand_value += scores[card[1]] 
        else: 
            hand_value += int(card[1])
    if ace and hand_value + 10 < 22:
        hand_value += 10
    return hand_value

def hand_over_cards(shuffled_list):
    #hand over cards 
    player_cards = []
    player_cards.extend([shuffled_list[0], shuffled_list[1]])
    print(calculate_hand(player_cards))


def main():
    game_begin()
    username = game_begin()
    original_card_deck = construct_card_deck()
    shuffled_card_deck = shuffle_card_deck(original_card_deck)
    card_deck_ready = remove_burning_cards(shuffled_card_deck)
    player_bet_money(username)



    

if __name__ == "__main__":
    main()












