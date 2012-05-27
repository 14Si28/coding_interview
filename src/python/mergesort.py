"""
Merge sort.

O(n log n).
"""
import sys

def merge_sort(values):
	def merge(values, p, q, r):
		n1 = q - p + 1
		n2 = r - q
		left = [None,]*(n1+1)
		right = [None,]*(n2+1)
		left[-1] = sys.maxint # sentinel
		right[-1] = sys.maxint

		for i in xrange(n1+1):
			left[i] = values[p+i-1]

		for j in xrange(n2+1):
			right[j] = values[q+j]

		i = 1
		j = 1
		for k in xrange(p, r+1):
			if left[i] <= right[j]:
				values[k] = left[i]
				i += 1
			else:
				values[k] = right[i]
				j += 1

	def msort(values, p, r):
		if p >= r:
			return

		q = (p+r)/2
		msort(values, p, q)
		msort(values, q+1, r)
		merge(values, p, q, r)

	msort(values, 0, len(values)-1)
	return values


def _test_one(input):
	expected = sorted(input)
	actual = merge_sort(input)
	print '{}'.format(actual)
	if not actual == expected:
		raise Exception('FAIL Expected: {} Actual: {}'.format(expected, actual))

def _test_all():
	_test_one(list('edcba'))
	_test_one(list('jklasdf'))
	_test_one(list('987654321'))
	a = list('abcdefghhijklkmnopqrstuvwxyz9876543210')
	random.shuffle(a)
	_test_one(a)
	print 'SUCCESS'

if __name__ == '__main__':
	_test_all()
 