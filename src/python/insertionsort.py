"""
Insertion sort.

O(n) best, O(n^2) worst.
"""
import random

def insertion_sort(values):
    for j in xrange(1, len(values)):
        key = values[j]
        i = j - 1
        while i >= 0 and values[i] > key:
            values[i+1] = values[i]
            i -= 1

        values[i+1] = key

    return values

def _test_one(input):
    expected = sorted(input)
    actual = insertion_sort(input)
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
 
