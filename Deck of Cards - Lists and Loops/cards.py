'''
   CS5001
   Fall 2022
   Elif Tirkes 
   Homework 4: Cards.py
'''

import random

def main():
    list = create_deck()
    # creates a deck of cards and assigns it into 'list'

    shuffled_list = shuffle(list)
    # shuffles the list of generated cards 

    players = int(input("How many players are there? (1-4)"))
    # gets the number of players/hands in the game from the user
    
    cards = int(input("How many cards are there per hand? (0-13)"))
    # gets the number of cards to hand out from the user

    print(shuffled_list)
    print(len(shuffled_list))
    
    print(deal(players, cards, shuffled_list))
    # prints the nested list of players and cards per player 


def create_deck():
    '''
    Function -- create_deck()
        Function creates an empty list called new_deck
        and in 4 for loops
        creates a set of cards for each suit and stores
        each suit in a temporary variable. Appends all 4 suits
        to the empty list new_deck. 
    Returns a list called new_deck with 52 playing cards,
    13 from each suit. 
    '''
    new_deck = []
    # creates an empty list to append generated suits
    
    values = ["2", "3", "4", "5", "6", "7", "8", 
              "9", "T", "J", "Q", "K", "A"]
    # 13 values 
    suits = ["s", "h", "d", "c"] 
    # 4 suits 
    
    # Making Spade Cards 
    for i in range(0, 13): 
        spades_holder = str(values[i]) + suits[0]
        # temporarily holds spade cards
        new_deck.append(spades_holder)
        # adds spade cards to deck list

    # Making Heart Cards 
    for i in range(0, 13): 
        hearts_holder = str(values[i]) + suits[1]
        # temporarily holds heart cards
        new_deck.append(hearts_holder)
        # adds heart cards to deck list

    # Making Diamonds Cards 
    for i in range(0, 13): 
        diamonds_holder = str(values[i]) + suits[2]
        # temporarily holds diamond cards
        new_deck.append(diamonds_holder)
        # adds diamonds cards to deck list

    # Making Club Cards 
    for i in range(0, 13): 
        clubs_holder = str(values[i]) + suits[3]
        # temporarily holds clubs cards
        new_deck.append(clubs_holder)
        # adds club cards to deck list

    return new_deck

def shuffle(cards):
    '''
    Function -- shuffle()
        Function creates a copy of the deck of cards to avoid
        modifying the original. Uses a random generator within
        0 - 52 (length of the deck of cards)
        to switch the placement of each card at index
        i with a randomly generated index i.
        Effectively shuffles the deck and
        returns a shuffled deck. 
    Parameters:
    list_of_cards -- list containing a deck of 52
    cards generated
    using the create_deck() function 
    Returns a copy of the deck of cards
    list called modifiable_list
    with shuffled values. 
    '''
    modifiable_list = cards.copy()
    # creates a copy of the deck of cards 
    # to avoid manipulating the original deck of cards list

    for i in range(len(modifiable_list)):
        number = random.randint(0, i)
        if number == i:
            continue
        modifiable_list[i], modifiable_list[number] = \
            modifiable_list[number], modifiable_list[i]
        # switches the index of each card with a random integer
        # within the range of the deck
        # to to simulate shuffling the deck 
        
    return (modifiable_list)


def deal(number_of_hands, number_of_cards, cards):
    '''
    Function -- deal()
        Function runs through the number of input players,
        and for every player, assigns a card from the shuffled
        deck starting from index 0, followed by index 0 plus
        one to simulate distributing a hand of
        cards to each player in turns. For loop
        also removes each added card from the main deck.
        After the nested for loop does this for
        each player for the value in
        number_of_cards, the function returns a nested list with
        each player's hand. 
        Parameters:
    players -- an int value from 1-4 representing the number of hands
    number_of_cards -- number of cards that'll be distributed to every player
    cards -- deck of shuffled cards from the shuffle() function 
    Returns a nested list of each player's hand. 
    '''
    cards_dealt = []

    for i in range(0, number_of_hands):
        temp_deck = []
        # cards given to each player per round of i iteration
        
        position = i
        # iteration for dealt cards 
        
        for j in range(number_of_cards):
            temp_deck.append(cards[position])
            # hands one card to
            # each player starting from the first card in the shuffled deck 
            position = position + 1
            # moves up a step, handing the required number of
            # cards to the player 
        cards_dealt.append(temp_deck)

    return cards_dealt
    

if __name__ == "__main__":
    main() 
