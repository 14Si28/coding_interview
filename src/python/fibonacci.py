"""
Generate Fibonacci numbers with two different implementations.
"the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two."

n: 0,1,2,3,4,5,6, 7, 8
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
    assert k > n
    # TODO base case
    seq = []
    prev = [0, 1]
    curr = 0
    while curr < k:
        curr = prev[1] + prev[0]
        prev[0] = prev[1]
        prev[1] = curr
        if curr >= n:
            seq.append(curr)

    return seq


def fibonacci_number(n):
    if n <= 1:
        return 0
    if n <= 3:
        return 1
    return fibonacci_number(n-2) + fibonacci_number(n-1)

#################################################
# Tests

def _fibonacci_check(expected, fib_func):
    n = len(expected)-1
    actual = fib_func(n)
    print 'Expected for n={} : {}'.format(n, ', '.join(['{}'.format(x) for x in expected]))
    print 'Actual: {}'.format(', '.join(['{}'.format(x) for x in actual]))
    for pair in zip(expected, actual):
        assert pair[0] == pair[1]
    assert len(expected) == len(actual)

def _test_fibonacci(fib_func):
    _fibonacci_check([0,1,1,2,3,5,8], fib_func)
    _fibonacci_check([0,1,1,2,3,5,8,13,21,34,55,89,144], fib_func)
    _fibonacci_check([0], fib_func)
    _fibonacci_check([0,1], fib_func)

if __name__ == '__main__':
    _test_fibonacci(fibonacci_recursive)
    _test_fibonacci(fibonacci_iterative)

    assert fibonacci_subsequence(8, 21) == [8, 13, 21]
    assert fibonacci_subsequence(2, 13) == [2, 3, 5, 8, 13]
    assert fibonacci_subsequence(0, 34) == [1, 2, 3, 5, 8, 13, 21, 34]

    assert fibonacci_number(5) == 3
    assert fibonacci_number(10) == 34
    assert fibonacci_number(13) == 144


