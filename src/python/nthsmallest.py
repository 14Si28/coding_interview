"""
Find the nth smallest integer in an array of integers.

Follow up question: make this work effeciently with billions of integers.
"""
import random

def nthsmallest_sort(numbers, n):
	"""
	Cheat and sort the list. 
	
	O(n log n)  (Timsort)
	"""
	if n < 0:
		raise ValueError('Invalid n')
	sorted_numbers = sorted(numbers) # could do numbers.sort() to sort in place and modify param
	return sorted_numbers[n]

def 

def nthsmallest(numbers, n):
	"""
	n is 0 based, n = 1 returns the 2nd smallest number.

	This is O(n^2) due to the extra sorts, since the bucket is incrementally sorted and of constant size once full. 
	This also uses extra storage of up to n.
	
	This is not a good solution.
	"""
	if n < 0:
		raise ValueError('invalid n')
	if len(numbers) < n:
		raise ValueError('n must be > len(numbers)')

	unsorted = True
	bucket = []
	index = 0
	while index < len(numbers):
		num = numbers[index]
		if len(bucket) <= n:
			# Fill the bucket with n numbers first
			bucket.append(num)
		else:
			if unsorted:
				bucket.sort()
				unsorted = False
				print bucket
			for bindex in xrange(len(bucket)):
				if num < bucket[bindex]:
					# Insert the new smaller number
					bucket.insert(bindex, num)
					# Evict the largest number
					bucket.pop()
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
	_test_one(func, [0,1,2,3,4,5,6,7,8], 0, 0)
	_test_one(func, [0,1], 1, 1)
	_test_one(func, [0,1], 0, 0)
	_test_one(func, [0], 0, 0)

if __name__ == '__main__':
	_test_all(nthsmallest)
	_test_all(nthsmallest_sort)

