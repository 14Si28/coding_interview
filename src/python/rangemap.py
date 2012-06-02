"""
Given an integer, return a string. There is an integer range that always returns a particular string for that range.

e.g.

* 1,2,3...9 => "kitten"
* 10,11,12..19 => "chicklet"
* 20,21,22..49 => "calf"
* 10000..393451 => "bunny"
* 393452..598274 => "puppy"

There is no pattern to the beginning or ending of each range, but the numbers within a range are guaranteed to be contiguous. 
The ranges are known up front, but assume there could be many millions of ranges.
"""

import random
import math

def rangemap_linear(ranges, target_number):
    """
    Blindly compare the ranges for each search.

    O(n)

    ranges: list of tuples, each tuple is a (int, int, str), first two ints 
        lower and upper inclusive bound on the range, string in the mapping for that range.
    
    target_number: number to map to a range

    returns: the str mapping
    """
    for range_data in ranges:
        if target_number >= range_data[0] and target_number <= range_data[1]:
            return range_data[2]
    return None

def rangemap_log(ranges, target_number):
    """
    Use concepts from binary search and quicksort to limit the range exploration to roughly half of the total ranges.
    We choose a pivot, compare the range, then explore the remaining half of ranges.

    O(log n)   after the initial sort.
    """
    def range_comparator(x, y):
        # Compare upper bound of range x to lower bound of y
        return cmp(x[1], y[0])

    # NOTE: We would sort the ranges once and cache them, since the problem description says the ranges are known up front.
    sorted_ranges = sorted(ranges, cmp=range_comparator)

    pivot = int(len(sorted_ranges)/2)
    for z in xrange(888): # Limit our search
        curr = sorted_ranges[pivot]
        print curr
        if curr[0] <= target_number <= curr[1]:
            # Found the range
            return curr[2]

        # If we're at the edge of all ranges and haven't matched, there is no match
        if pivot == 0 or pivot == len(sorted_ranges) - 1:
            return None

        # Explore either the lower half or the upper half of the remaining ranges
        if target_number < curr[0]:
            pivot = int(pivot/2.0)
        else:
            assert target_number > curr[1]
            pivot = int(math.ceil(pivot*(1.5)))
            print pivot

    raise Exception('Search failed.')

def _test_one(func, ranges, target_number, expected):
    # Randomize the ranges
    ranges = list(ranges)
    random.shuffle(ranges)

    actual = func(ranges, target_number)
    print '{} , {}  ===>   {}'.format(ranges, target_number, actual)
    if actual != expected:
        raise Exception('FAIL: Expected: {}   Actual: {} '.format(expected, actual))

def _test_all(func):
    ranges1 = [(1,9, 'kitten'), (10, 19, 'chicklet'), (20,49, 'calf'), (10000,393451, 'bunny'), (393452,598274, 'puppy')]
    _test_one(func, ranges1, 8, 'kitten')
    _test_one(func, ranges1, 380000, 'bunny')
    _test_one(func, ranges1, -30, None)
    # TODO More test cases.
    print 'SUCCESS {}'.format(func)

if __name__ == '__main__':
    _test_all(rangemap_linear)
    _test_all(rangemap_log)

