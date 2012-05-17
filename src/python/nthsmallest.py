"""
Find the nth smallest integer in an array of integers.
"""
import random

def nthsmallest(numbers, n):
	"""
	n is 0 based, n = 1 returns the 2nd smallest number.
	"""
	if n < 0:
		raise ValueError('invalid n')
	if len(numbers) < n:
		raise ValueError('n must be > len(numbers)')

	bucket = []
	index = 0
	while index < len(numbers):
		num = numbers[index]
		if len(bucket) <= n:
			# Fill the bucket with n numbers first
			bucket.append(num)
			bucket.sort()
		else:
			for bindex in xrange(len(bucket)):
				if num < bucket[bindex]:
					bucket.pop()
					bucket.append(num)
					bucket.sort()
					break
		print bucket
		index += 1

	return bucket[-1]

def _test_one(func, numbers, n, expected):
	random.shuffle(numbers)
	actual = func(numbers, n)
	if actual != expected:
		raise Exception('FAIL Expected: {}    Actual: {}'.format(expected, actual))
	print '{} , {}   =====>   {}'.format(numbers, n, actual)

def _test_all(func):
	_test_one(func, [0,1,2,3,4,5,6,7,8], 2, 2)
	_test_one(func, [0,1,2,3,4,5,6,7,8], 8, 8)
	_test_one(func, [0,1,2,3,4,5,6,7,8], 1, 1)
	_test_one(func, [0,1], 1, 1)
	_test_one(func, [0,1], 0, 0)
	_test_one(func, [0], 0, 0)

if __name__ == '__main__':
	_test_all(nthsmallest)
