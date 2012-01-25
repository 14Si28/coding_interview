"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
"""

def zero_matrix(matrix):
    """
    matrix: array of arrays, each element is an int. [ [0,0,1], [1,1,0] ]
    """
    if not matrix:
        return []
    to_zero_x = set()
    to_zero_y = set()
    width = len(matrix[0])
    height = len(matrix)
    for y in xrange(height):
        for x in xrange(width):
            if len(matrix[y]) != width:
                raise Exception('Invalid row width. Expected: {}  Actual: {}'.format(width, len(matrix[y])))
            if not matrix[y][x]: # if == 0
                # Track rows/cols to zero but don't zero yet.
                # If we zero'd rows/cols now, we'd detect the new zeros later,
                # and subsequent rows/cols would be zero'd incorrectly.
                to_zero_x.add(x)
                to_zero_y.add(y)

    for tx in to_zero_x:
        for y in xrange(height):
            matrix[y][tx] = 0
    for ty in to_zero_y:
        for x in xrange(width):
            matrix[ty][x] = 0
    return matrix


#################################
# Tests
#

def _check_zero_func(func, input, expected):
    def fail(context, expected, actual, input):
        raise AssertionError(
            'FAIL: {} Expected: {}   Actual: {}   Input: {}'.format(context, expected, actual, input))
    actual = func(input)
    for arr in zip(expected, actual):
        if len(arr[0]) != len(arr[1]):
            fail('Matrix sizes do not match.', expected, actual, input)
        for nums in zip(arr[0], arr[1]):
            if nums[0] != nums[1]:
                fail('Element value does not match.', expected, actual, input)

def _test_rotate_all(func):
    _check_zero_func(func, [[]], [[]])
    _check_zero_func(func, [[0]], [[0]])
    _check_zero_func(func, [[0,1]], [[0,0]])
    _check_zero_func(func, [[1,0]], [[0,0]])

    _check_zero_func(func, [[0,0],[1,1]], [[0,0], [0,0]])
    _check_zero_func(func, [[0,1],[1,1]], [[0,0], [0,1]])
    _check_zero_func(func, [[1,0],[1,1]], [[0,0], [1,0]])
    _check_zero_func(func, [[1,1],[1,1]], [[1,1], [1,1]])

    _check_zero_func(func, [[1,1],[0,1]], [[0,1], [0,0]])
    _check_zero_func(func, [[1,1],[1,0]], [[1,0], [0,0]])
    _check_zero_func(func, [[1,0],[0,1]], [[0,0], [0,0]])

    _check_zero_func(func, [[1,1,1], [1,1,1]], [[1,1,1], [1,1,1]])
    _check_zero_func(func, [[1,1,0], [1,1,1]], [[0,0,0], [1,1,0]])

    _check_zero_func(func, [[1,1,0], [1,1,1], [1,1,1]], [[0,0,0], [1,1,0], [1,1,0]])


if __name__ == '__main__':
    _test_rotate_all(zero_matrix)
    print 'SUCCESS'





