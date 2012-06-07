"""
Design and implement a deck of playing cards. 
(52 card deck, 4 suits, no jokers)
"""
import random

# If we used classes to represent the cards and deck, things are more verbose than if we just use a list of ints.
class Card(object):
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

class Deck(object):
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        raise Exception('Not implemented.')

# If we represent the cards as numbers 1 to 52 inclusive, 
# we get these regions for the suits:
#
#    HEARTS        ; SPADES   ; DIAMONDS
# 1 - 9, J, Q, K, A; 1 ..     ; 
# 1 ..           13; 14 .. 26 ; 27 ..
#

# We can map the suits to 52 cards as multiples of 13.
# e.g. 50 / 13 = 3 which is CLUB
HEARTS = 0
SPADES = 1
DIAMONDS = 2
CLUBS = 3

SUIT_NAMES = {
    HEARTS: 'hearts',
    SPADES: 'spades',
    DIAMONDS: 'diamonds',
    CLUBS: 'clubs'
}

CARD_NAMES = {
    1: 'ace',
    11: 'jack',
    12: 'queen',
    13: 'king'
}

def create_deck():
    return range(1,52+1)

def check_card_valid(card):
    if card <= 0 or card > 52:
        raise ValueError('Invalid card: {}'.format(card))

def card_value(card):
    check_card_valid(card)
    return ((card-1) % 13)+1    

def suit(card):
    check_card_valid(card)
    return (card-1) / 13

def card_name(card):
    cval = card_value(card)
    if cval in CARD_NAMES:
        return CARD_NAMES[cval]
    return cval

def print_cards(cards):
    for card in cards:
        print '{} of {}'.format(card_name(card), SUIT_NAMES[suit(card)])

def main():
    cards = create_deck()
    assert len(cards) == 52
    
    print '________________ Sorted deck:'
    print_cards(cards)
    print '________________ Shuffled deck:'
    random.shuffle(cards)
    print_cards(cards)


if __name__ == '__main__':
    main()

