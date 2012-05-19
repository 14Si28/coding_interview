"""
Given a dictionary of words (English and other languages), then given an input search term, 
determine all valid words that differ by only one character 
(anywhere in the input term). No additional characters are added, 
i.e. the length of the search term matches the length of the alternate words.

"lair"  ==> fair, airy,  ...
"ball" ==> fall, wall, tall, bail, Bali ...

Follow up: what if the dictionary has hundreds of millions of words?
Variation: what if you must generate the variations? 
"""
import re

TERM1 = 'ball'
MATCHES1 = {
	# Variant matches
	'ball',
	'fall',
	'wall',
	'tall',
	'bail',
	'Bali',
	'call',
	'bill',
	'mall'
}
NONMATCHES1 = {
	# Non matches
	'ballroom',
	'caller',
	'bark',
	'bar',
	'ba',
	'b',
	'all',
	'tail',
}
DICTIONARY1 = MATCHES1.union(NONMATCHES1)

BALL_RE = re.compile(r'^(.{1}all|b.{1}ll|ba.{1}l|bal.{1}){1}$')

def find_variants(search_term, term_set):
	matches = set()
	for t in term_set:
		if re.match(BALL_RE, t):
			matches.add(t)
	return matches

def _test_one(func, search_term, term_set, expected_set):
	actual = func(search_term, term_set)
	print '{}  ===>   {}'.format(search_term, sorted(actual))
	

def _test_all():
	_test_one(find_variants, TERM1, DICTIONARY1, MATCHES1)

if __name__ == '__main__':
	_test_all()




