"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?
"""

# Examples here assume counter-clockwise, since that's what numpy does by default.

def rotate_cheat(pixel_matrix):
    """
    pixel_matrix: array of arrays, each int element represents a pixel. [ [0,0,1], [1,1,0] ]
    """
    import numpy
    return numpy.rot90(pixel_matrix)

def rotate_naive(pixel_matrix):
    pass



#################################
# Tests
#

def _check_rotate_func(func, input, expected):
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
    _check_rotate_func(func, [[]], [[]])
    _check_rotate_func(func, [[0]], [[0]])
    _check_rotate_func(func, [[0,1]], [[1], [0]])
    _check_rotate_func(func, [[0,1], [7,8]], [[1,8], [0, 7]])
    _check_rotate_func(func, [[0,1,2], [7,8,9]], [[2,9], [1,8], [0,7]])

if __name__ == '__main__':
    _test_rotate_all(rotate_cheat)
    print 'SUCCESS'




