"""
Quicksort illustration. 

There are many quicksort variations and tweaks; this file just covers some basics.

Note: in Python use sorted() instead (Timsort).
"""
import itertools

def quicksort(values):
    """
    Average case O(n log n). Memory usage O(n).
    """
    if len(values) <= 1:
        return values 

    #print values # Uncomment this to see the divide and conquer progression.

    left = []
    right = []
    # Naive pivot selection.
    pivot_ind = int(len(values) / 2) 
    pivot = values[pivot_ind]
    pivot_list = []

    for ind in range(0, len(values)):
        x = values[ind]
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            assert x == pivot
            pivot_list.append(x)

    return quicksort(left) + pivot_list + quicksort(right)

def _test(func, input):
    expected = sorted(input)
    actual = func(input)
    print '{}    ===>    {}'.format(input, list(actual))
    if actual != expected:
        raise Exception('FAIL Expected: {}    Actual:   {}'.format(expected, actual))

def _test_all(func):
    _test(func, [1, 0])
    _test(func, [0, 3, 2, 1, 4, 5, 7, 6, 8])
    _test(func, [0, 3, 2, 1, 4, 5, 5, 5, 5, 5, 7, 6, 8])
    _test(func, [0, 1])
    _test(func, [0, 1, 2])
    _test(func, [2, 1, 0])
    _test(func, [2, 0, 1])
    _test(func, [0, 3, 2, 1, 4, 5, 7, 6, 8]*3)

if __name__ == '__main__':
    _test_all(quicksort)



