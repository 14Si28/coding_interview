"""
Merge sort.

O(n log n), stable.
"""
import random

def merge_sort(values):
    # From: http://rosettacode.org/wiki/Sorting_algorithms/Merge_sort#Python

    # Note: you could reuse Python's heapq.merge()
    def merge(left, right):
        result = []
     
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
     
        if right:
            result.extend(right)
        if left:
            result.extend(left)
        return result

    def msort(m):
        if len(m) <= 1:
            return m
     
        middle = len(m) / 2
        left = m[:middle]
        right = m[middle:]
     
        left = msort(left)
        right = msort(right)
        return list(merge(left, right))

    return msort(values)

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
 
