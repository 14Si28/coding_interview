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


