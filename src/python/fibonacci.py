"""
Generate Fibonacci numbers with two different implementations.
"the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two."
0,1,1,2,3,5,8,13,21,34,55,89,144
"""

def fibonacci_recursive(n):
    if n <= 1:
        return [0]
    return fibonacci_recursive_impl(n-2, [0,1])

def fibonacci_recursive_impl(n, seq):
    if n <= 0 or len(seq) < 2:
        return seq
    x = seq[-1] + seq[-2]
    seq.append(x)
    return fibonacci_recursive_impl(n-1, seq)



def fibonacci_iterative(n):
    if n <= 1:
        return [0]
    seq = [0,1]
    for m in xrange(n-2):
        x = seq[-1] + seq[-2]
        seq.append(x)
    return seq


def fibonacci_sequence(n, k):
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
    actual = fib_func(len(expected))
    print 'Expected: {}'.format(', '.join(['{}'.format(x) for x in expected]))
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

    assert fibonacci_sequence(8, 21) == [8, 13, 21]
    assert fibonacci_sequence(2, 13) == [2, 3, 5, 8, 13]
    assert fibonacci_sequence(0, 34) == [1, 2, 3, 5, 8, 13, 21, 34]

    assert fibonacci_number(5) == 3
    assert fibonacci_number(10) == 34
    assert fibonacci_number(13) == 144


