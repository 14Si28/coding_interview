"""
Implement a fair randomized shuffling algorithm for a deck of cards.
"""

import random

def shuffle_cheat(cards):
	"""
	Cheat and use Python's shuffle.
	"""
	return random.shuffle(cards)

def shuffle_fisher(cards):
	"""
	Fisher-Yates shuffling algorithm (aka Knuth shuffle).
	"""
	for i in xrange(len(cards)-1, -1, -1):
		j = random.randint(0, i)
		cards[i], cards[j] = cards[j], cards[i]

def create_cards():
	return list(range(52))

def _test_one(func):
	cards = create_cards()
	print '{}'.format(func)
	func(cards)
	print cards

if __name__ == '__main__':
	_test_one(shuffle_cheat)
	_test_one(shuffle_fisher)



	
