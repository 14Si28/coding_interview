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

# Illustrates an algorithm.
def rotate_copy(pixel_matrix):
    """
    Rotate 90 degrees counter-clockwise by creating a copy.
    pixel_matrix: array of arrays, each int element represents a pixel. [ [0,0,1], [1,1,0] ]
    """
    if not pixel_matrix:
        return []
    old_width = len(pixel_matrix[0])
    rotated = []
    for old_col in xrange(old_width-1, -1, -1): # width-1 to 0
        rotated.append([])
        new_row = rotated[-1]
        for arr in pixel_matrix:
            if len(arr) != old_width:
                raise Exception('Invalid row width. Expected: {}  Actual: {}'.format(old_width, len(arr)))
            new_row.append(arr[old_col])
    return rotated

def rotate_in_place(pixel_matrix):
    """
    In place rotation, by swapping outermost edges to innermost (concentric).
    """
    # TODO
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
    _test_rotate_all(rotate_copy)
    print 'SUCCESS'




