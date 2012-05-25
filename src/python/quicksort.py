"""
Quicksort illustration. 

There are many quicksort variations and tweaks; this file just covers some basics.

Note: in Python use sorted() instead (Timsort).
"""
import random

def quicksort(values):
    """
    Perform a quick sort without modifying the original list.

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


def quicksort_in_place(values):
    """
    O(n log n) with constant additional memory. (Other than the recursion stacks!)

    Reference: Introduction to Algorithms section 7.1
    """
    def qs(start, end):
        if start >= end:
            return
        # print values  # Uncomment this to see the divide and conquer progression.
        q = partition(start, end)
        qs(start, q-1)
        qs(q+1, end)

    def partition(start, end):
        pivot = values[end]
        i = start - 1
        for j in xrange(start, end):
            if values[j] <= pivot:
                i += 1
                # swap
                values[i], values[j] = values[j], values[i]

        values[i+1], values[end] = values[end], values[i+1]
        return i+1

    qs(0, len(values)-1)
    return values

def quicksort_in_place_random(values):
    """
    Use a random pivot.

    O(n log n).

    Reference: Introduction to Algorithms section 7.3
    """
    def qs(start, end):
        if start >= end:
            return
        # print values  # Uncomment this to see the divide and conquer progression.
        q = random_partition(start, end)
        qs(start, q-1)
        qs(q+1, end)

    def partition(start, end):
        pivot = values[end]
        i = start - 1
        for j in xrange(start, end):  # end is exclusive, i.e. end will not be included in the range
            if values[j] <= pivot:
                i += 1
                values[i], values[j] = values[j], values[i]  # swap

        values[i+1], values[end] = values[end], values[i+1]
        return i+1

    def random_partition(start, end):
        assert start < end
        i = random.randint(start, end) # randint is inclusive, end is included in the possible ints
        values[end], values[i] = values[i], values[end]  # Swpa the random pivot with the end
        return partition(start, end)

    qs(0, len(values)-1)
    return values

def _test(func, input):
    expected = sorted(input)
    actual = func(input)
    print '{}    ===>    {}'.format(input, list(actual))
    if actual != expected:
        raise Exception('FAIL Expected: {}    Actual:   {}'.format(expected, actual))

def _test_all(func):
    print '____ Function: {}'.format(func)
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
    _test_all(quicksort_in_place)
    _test_all(quicksort_in_place_random)



