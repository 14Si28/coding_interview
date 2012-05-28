"""
A child running up a staircase with n steps can hop either 1, 2 or 3 steps at a time. 
Implement a method to count the possible ways the child can run up the stairs.
"""

def countways(n):
	"""
	O(n^3)
	"""
	if n <= 0:
		return 0
	if n == 1:
		return 1

	return countways(n-1) + countways(n-2) + countways(n-3)

def countways2(n, cache=None):
	if n <= 0:
		return 0
	if not cache:
		cache = { 0: 0, 1: 1}
	if n in cache:
		return cache[n]

	q = countways2(n-1, cache) + countways2(n-2, cache) + countways2(n-3, cache)
	cache[n] = q
	return q

def _test_one(func, input, expected):
	actual = func(input)
	print ' {} ==> {}'.format(input, actual)
	if actual != expected:
		raise Exception('FAIL expected {}  actual {} '.format(expected, actual))

def _test_all(func):
	_test_one(func, 0, 0)
	_test_one(func, 1, 1)
	_test_one(func, 2, 1)
	_test_one(func, 3, 2)
	_test_one(func, 4, 4)
	_test_one(func, 5, 7)
	_test_one(func, 6, 13)
	_test_one(func, 7, 24)
	_test_one(func, 8, 44)
	_test_one(func, 9, 81)
	_test_one(func, 10, 149)
	_test_one(func, 11, 274)
	_test_one(func, 12, 504)
	_test_one(func, 13, 927)
	_test_one(func, 14, 1705)

if __name__ == '__main__':
	_test_all(countways)
	_test_all(countways2)

