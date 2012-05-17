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
    if n <= 0:
        raise ValueError('Invalid n')
    return sorted(numbers)[n-1] # could do numbers.sort() to sort in place and modify param

def nthsmallest_select(values, n):
    """
    Use a variant of quicksort that only sorts one side of the partition.

    O(n)

    Reference: Introduction to Algorithms section 9.2
    """
    def partition(start, end):
    	# print values # Uncomment to watch the divide and conquer
        pivot = values[end]
        i = start - 1
        for j in xrange(start, end):  # end is exclusive, i.e. end will not be included in the range
            if values[j] <= pivot:
                i = i + 1
                values[i], values[j] = values[j], values[i]  # swap

        values[i+1], values[end] = values[end], values[i+1]
        return i+1

    def random_partition(start, end):
        assert start < end
        i = random.randint(start, end) # randint is inclusive, end is included in the possible ints
        values[end], values[i] = values[i], values[end]  # Swap the random pivot with the end
        return partition(start, end)

    def random_select(start, end, i):
        if start == end:
            return values[start]
        pivot = random_partition(start, end)
        k = pivot - start + 1
        if i == k:
            return values[pivot]
        elif i < k:
            return random_select(start, pivot-1, i)
        else:
            return random_select(pivot+1, end, i-k)

    return random_select(0, len(values)-1, n)

def _test_one(func, numbers, n, expected):
    random.shuffle(numbers)
    actual = func(numbers, n)
    if actual != expected:
        raise Exception('FAIL Expected: {}    Actual: {}'.format(expected, actual))
    print '{} , {}   =====>   {}'.format(numbers, n, actual)

def _test_all(func):
    print '_________ Func: {}'.format(func)
    _test_one(func, [0,1,2,3,4,5,6,7,8], 3, 2)
    _test_one(func, [0,1,2,3,4,5,6,7,8], 9, 8)
    _test_one(func, [0,1,2,3,4,5,6,7,8], 2, 1)
    _test_one(func, [0,1,2,3,4,5,6,7,8], 1, 0)
    _test_one(func, [0,1], 2, 1)
    _test_one(func, [0,1], 1, 0)
    _test_one(func, [0], 1, 0)

if __name__ == '__main__':
    _test_all(nthsmallest_sort)
    _test_all(nthsmallest_select)

