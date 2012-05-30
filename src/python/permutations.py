"""
Generate all permutations of characters in a given input string, e.g. 'ab' ==> { 'ab', 'ba' }
"""

# Note: Python's itertools provides permutations() and combinations(), so you would normally not reimplement these yourself. 
#
# Trivia: There's also math.factorial()
# Definitions refresher: 
#  n choose r: n items, choosing r for each permutation/combination.
#  Permutations: order matters. 'ab' and 'ba' are distinct. With repetitions: n^r. Without repitition: n! / (n - r)!
#  Combinations: order does not matter. 'ab' = 'ba'. Without repitition: n! / ( r! (n - r)! ). With reptition: (n + r - 1)! / ( r! (n - 1)! )

def permute(input):
	if not input:
		return set()
	if len(input) == 1:
		return set(input)

	c = input[-1]
	substr_permutations = permute(input[0:-1])
	results = set()
	for r in substr_permutations:
		#print r
		for index in xrange(len(r)+1):
			rlist = list(r)
			rlist.insert(index, c)
			results.add(''.join(rlist))
	return results

def _test_one(func, input, expected):
	actual = func(input)
	actual = sorted(actual)
	expected = sorted(expected)
	print '{}  ===>   {}'.format(input, actual)
	if actual != expected:
		raise Exception('FAIL. Expected: {}   Actual: {}'.format(expected, actual))

def _test_all(func):
	_test_one(func, 'a', {'a'})
	_test_one(func, 'ab', {'ab', 'ba'})
	_test_one(func, 'abc', {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'})
	_test_one(func, 'abcd', {'abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'})

if __name__ == '__main__':
	_test_all(permute)