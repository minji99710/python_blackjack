#blackjack game
import itertools
import random
#start : greet, make card deck, shuffle the card 
greeting = 'Hello, welcome to bichon casino! Let me introduce your dealer today, kimbision.'
print(greeting)

username = input('What is your name, sir? : ')
print('\nNice to meet you {name}, it\'s a perfect day to gamble! \
\nHave a good time with your puriti gambling bichon :)'.format(name=username))

#add a card deck 
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['spades', 'clovers', 'diamonds', 'hearts']

original_deck = list(itertools.product(suits, vals))
original_deck_with_values = {}
shuffled_list = random.sample(original_deck, len(original_deck))
print('\ncards are all shuffled! \n')

#remove the burning card 
burning_card = []
burning_card.extend([shuffled_list[0], shuffled_list[1]])
del shuffled_list[0:2] 
print('the burning cards have been removed ! It seems like we are all ready.\n')

#player bet money
player_money = 100
player_bet = input('How much would you bet, sir {name}? (you currently have $100): '.format(name=username))
player_money -= int(player_bet)
print('you have bet ${bet_money}, and now have ${player_money} left.'.format(bet_money=player_bet, player_money=player_money))
player_state = ''












