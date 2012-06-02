"""
Given an array of integers, return a new array where each element is 
the product of all other elements from the original array except that index.

e.g.
Given [3, 8, 2]
Return [16, 6, 24]
Which is [(8*2), (3*2), (3*8)]

Follow up questions: Can you make it O(n)? How would you test it for correctness? What about negative numbers and 0's?
"""

def products(numbers):
    if not numbers:
        return []

    product = None # Wait to init product
    zero_index = -1
    for index in xrange(len(numbers)):
        x = numbers[index]
        if x:
            if not product:
                product = 1 # Lazy init product to 1 so that we can handle the single zero element case further below.

            product *= x
        elif zero_index < 0:
            # Avoid zeroing out the product
            zero_index = index
        else:
            # Multiple 0's in the input mean the entire results are 0, we can short circuit out.
            return [0,]*len(numbers)

    results = []
    if zero_index >= 0:
        results = [0,]*len(numbers)
        results[zero_index] = product if product else 0
    else:
        for x in numbers:
            assert x # != 0
            results.append(product/x)
    
    return results

def _test_one(func, input, expected):
    actual = func(input)
    print '{}  ===> {}'.format(input, actual)
    if actual != expected:
        raise Exception('FAIL Expected: {}   Actual: {}'.format(expected, actual))

def _test_all(func):
    _test_one(func, [3,8,2], [16, 6, 24])
    _test_one(func, [1,2,3,4,5,6,7,8], [40320, 20160, 13440, 10080, 8064, 6720, 5760, 5040])
    _test_one(func, [3,0,2], [0, 6, 0])
    _test_one(func, [1,0,3,0,5], [0,0,0,0,0])
    _test_one(func, [1], [1])
    _test_one(func, [0], [0])
    _test_one(func, [], [])
    _test_one(func, [1,2], [2,1])
    _test_one(func, [-1,2], [2,-1])
    _test_one(func, [-1,2,-3], [-6,3,-2])

if __name__ == '__main__':
    _test_all(products)

        










