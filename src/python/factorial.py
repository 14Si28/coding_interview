"""
Write an algorithm to compute n factorial (n!).
"""

import math

# Normally you would use math.factorial.
#
# Reminder, factorial is: n * (n - 1) * (n - 2) ... * 1
#

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

def factorial_iterative(n):
    if n <= 1:
        return 1
    result = 1
    for x in xrange(n, 0, -1):
        result *= x

    return result

def _test_one(func, n):
    expected = math.factorial(n)
    actual = func(n)
    print '{}  ===> {}   ?   {}'.format(n, expected, actual)
    if expected != actual:
        raise Exception('FAIL For n: {} Expected: {}   Actual:  {}'.format(n, expected, actual))

def _test_all(func):
    for x in xrange(30):
        _test_one(func, x)

if __name__ == '__main__':
    _test_all(factorial_recursive)
    _test_all(factorial_iterative)


