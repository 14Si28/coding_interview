"""
Write an algorithm that calculates the total number of zeros in n factorial (n!).

Variant: count only the trailing zeros.
"""
import math
import re

def factorial_trailing_zeros(n):
    # 5 * 2 = 10   # one zero
    # 25 = 5 * 5   # extra 5 can pair with another multiple of 2 to get another zero
    if n < 0:
        return 0

    count = 0
    i = 5
    while n / i > 0:
        count += int(n / i)
        i *= 5

    return count

def factorial_total_zeros(n):
    # TODO impl
    return _total_zeros(n)[0]

############################

def _total_zeros(n):
    nfact = str(math.factorial(n))
    return nfact.count('0'), nfact

TRAILING_ZEROS_RE = re.compile(r'(0+)$')

def _trailing_zeros(n):
    nfact = str(math.factorial(n))
    match = re.search(TRAILING_ZEROS_RE, nfact)
    if match:
        zeros_str = match.group(1)
        return zeros_str.count('0'), nfact
    return 0, nfact

def _test_one(func, n, validation_func):
    expected, nfact = validation_func(n)
    actual = func(n)
    print '{}  ===> n!: {}   {}   ?   {}'.format(n, nfact, expected, actual)
    if expected != actual:
        raise Exception('FAIL For n: {}  n!: {}    Expected: {}   Actual:  {}'.format(n, nfact, expected, actual))

def _test_all(func, validation_func):
    print '___________ {}'.format(func)
    for x in xrange(30):
        _test_one(func, x, validation_func)

if __name__ == '__main__':
    _test_all(factorial_trailing_zeros, _trailing_zeros)
    _test_all(factorial_total_zeros, _total_zeros)

