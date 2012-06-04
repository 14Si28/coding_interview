"""
Generate Fibonacci numbers with two different implementations.
"the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two."

n: 0,1,2,3,4,5,6, 7, 8, 9,10,11, 12
f: 0,1,1,2,3,5,8,13,21,34,55,89,144
"""

def fibonacci_iterative(n):
    """
    returns: a list of n fibonacci numbers
    """
    if n <= 0:
        return [0]
    seq = [0,1]
    for m in xrange(n-1):
        x = seq[-1] + seq[-2]
        seq.append(x)
    return seq


def fibonacci_recursive(n, seq=None):
    """
    returns: a list of n fibonacci numbers
    """
    if seq == None:
        if n <= 0:
            seq = [0]
        else:
            seq = [0,1]

    if n <= 1:
        return seq

    seq.append(seq[-1] + seq[-2])
    return fibonacci_recursive(n-1, seq)


def fibonacci_subsequence(n, k):
    """
    Generate the Fibonacci sequence from n to k inclusive. n and k must be Fibnacci numbers.
    """
    if n > k or n < 0 or k < 0:
        raise ValueError('Invalid range. Must be 0 <= n <= k')

    seq = []

    if n <= 0:
        seq.append(0)
    if n == 1 or (n == 0 and k >=1):
        seq.append(1)

    prev = [0, 1]
    curr = 0
    while curr < k:
        curr = prev[1] + prev[0]
        prev[0] = prev[1]
        prev[1] = curr
        if curr >= n:
            seq.append(curr)

    return seq

def fibonacci_subsequence_by_index(n, k):
    """
    Generate the Fibonacci sequence from index n to k inclusive. The index is 0 based. n=0 k=0 returns [0].
    """
    if n > k or n < 0 or k < 0:
        raise ValueError('Invalid range. Must be 0 <= n <= k')

    seq = []
    if n == 0:
        seq.append(0)
    if n == 1 or (n == 0 and k >= 1):
        seq.append(1)

    prev = [0, 1]
    for x in xrange(2, k+1):
        curr = prev[1] + prev[0]
        prev[0] = prev[1]
        prev[1] = curr
        if x >= n:
            seq.append(curr)

    return seq

def fibonacci_number(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fibonacci_number(n-2) + fibonacci_number(n-1)

#################################################
# Tests

def _fibonacci_check(expected, fib_func):
    n = len(expected)-1
    actual = fib_func(n)
    print 'n={}  ===> {}'.format(n, actual)
    for pair in zip(expected, actual):
        assert pair[0] == pair[1]
    assert len(expected) == len(actual)

def _test_fibonacci(fib_func):
    print '___________ {}'.format(fib_func)
    _fibonacci_check([0,1,1,2,3,5,8], fib_func)
    _fibonacci_check([0,1,1,2,3,5,8,13,21,34,55,89,144], fib_func)
    _fibonacci_check([0], fib_func)
    _fibonacci_check([0,1], fib_func)

def _test_subsequence(func, n, k, expected):
    actual = func(n, k)
    print 'n={}, k={}  ===> {}'.format(n, k, actual)
    if expected != actual:
        raise Exception('FAIL For n={}, k={} Expected: {}  Actual: {}'.format(n, k, expected, actual))

def _test_all_subsequence():
    print '___________ {}'.format(fibonacci_subsequence)
    _test_subsequence(fibonacci_subsequence, 0, 1, [0,1, 1])
    _test_subsequence(fibonacci_subsequence, 0, 0, [0])
    _test_subsequence(fibonacci_subsequence, 1, 1, [1, 1])
    _test_subsequence(fibonacci_subsequence, 0, 2, [0,1,1,2])
    _test_subsequence(fibonacci_subsequence, 1, 3, [1, 1, 2, 3])
    _test_subsequence(fibonacci_subsequence, 8, 21, [8, 13, 21])
    _test_subsequence(fibonacci_subsequence, 2, 13, [2, 3, 5, 8, 13])
    _test_subsequence(fibonacci_subsequence, 0, 34, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    print '___________ {}'.format(fibonacci_subsequence_by_index)
    _test_subsequence(fibonacci_subsequence_by_index , 0, 1, [0,1])
    _test_subsequence(fibonacci_subsequence_by_index , 0, 0, [0])
    _test_subsequence(fibonacci_subsequence_by_index , 1, 1, [1])
    _test_subsequence(fibonacci_subsequence_by_index , 1, 2, [1,1])
    _test_subsequence(fibonacci_subsequence_by_index , 0, 2, [0,1,1])
    _test_subsequence(fibonacci_subsequence_by_index , 0, 3, [0,1,1,2])
    _test_subsequence(fibonacci_subsequence_by_index , 1, 3, [1, 1, 2])

if __name__ == '__main__':
    _test_fibonacci(fibonacci_recursive)
    _test_fibonacci(fibonacci_iterative)

    _test_all_subsequence()

    assert fibonacci_number(5) == 5
    assert fibonacci_number(10) == 55
    assert fibonacci_number(12) == 144


