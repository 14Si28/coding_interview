"""
Write methods to imiplement multiply, subtract, and divide operations for integers using only the add operator.
"""

def multiply_op(left, right):
    if left == 0 or right == 0:
        return 0
    if left == 1:
        return right
    if right == 1:
        return left

    result = left
    for x in xrange(abs_op(right)-1):
        result += left

    if right < 0:
        result = negate(result)
    return result

def abs_op(num):
    """
    returns: abs(num)
    """
    if num < 0:
        return negate(num)

    return num

def negate(num):
    z = 1 if num < 0 else -1
    result = 0
    detector = num
    while detector != 0:
        result += z
        detector += z

    return result

def divide_op(numer, denom):  # dividend, divisor
    """
    returns: numer / denom
    """
    if denom == 0:
        raise ValueError('Division by 0 is naughty.')
    if numer == 0:
        return 0
    
    abs_numer = abs_op(numer)
    abs_denom = abs_op(denom)
    product = 0
    result = 0
    while product + abs_denom <= abs_numer:
        product += abs_denom
        result += 1

    if (numer < 0 and denom < 0) or (numer > 0 and denom > 0):
        return result

    return negate(result)

def _assert_equals(expected, actual, context):
    if actual != expected:
        raise Exception('FAIL Expected: {}  Actual: {}  Context: {}'.format(expected, actual, context))

def _test_all():
    print '_________ {}'.format(negate)
    for x in xrange(-2,2):
        _assert_equals(-1*x, negate(x), x)

    print '_________ {}'.format(multiply_op)
    for x in xrange(-10,10):
        for y in xrange(-10,10):
            print ' {} * {} = {} '.format(x, y, multiply_op(x, y))
            _assert_equals(x*y, multiply_op(x, y), [x, y])

    print '_________ {}'.format(divide_op )
    for x in xrange(-10,10):
        for y in xrange(-10,10):
            if y != 0:
                print ' {} * {} = {} '.format(x, y, divide_op (x, y))
                _assert_equals(int((1.0*x)/(1.0*y)), divide_op (x, y), [x, y])

    print 'SUCCESS'

if __name__ == '__main__':
    _test_all()