"""
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to
isSubstring (i.e., waterbottle is a rotation of erbottlewat).
"""

# "Rotation" might be more accurately described as shifting or sliding.

# isSubstring in python is string.find() >= 0
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    # Magic: concatenate s2 twice.
    # s1 = ab, s2 = ba, s3 = baba; note s1 ab appears in middle bABa, always.
    s3 = '{}{}'.format(s2, s2)
    return s3.find(s1) >= 0

#################################
# Tests
#

def _check_rotation_func(func, s1, s2, expected):
    actual = func(s1, s2)
    if actual != expected:
        raise AssertionError(
            'FAIL: Expected: {}   Actual: {}   Input s1: {}   s2: {}'.format(expected, actual, s1, s2))

def _test_rotation_all(func):
    _check_rotation_func(func, '', '', True)
    _check_rotation_func(func, 'a', 'a', True)
    _check_rotation_func(func, 'ab', 'ba', True)
    _check_rotation_func(func, 'ab', 'ab', True)
    _check_rotation_func(func, 'abc', 'bca', True)
    _check_rotation_func(func, 'abc', 'bac', False)
    _check_rotation_func(func, 'ab', 'a', False)
    _check_rotation_func(func, 'waterbottle', 'erbottlewat', True)
    _check_rotation_func(func, 'waterbottle', 'erbottlewta', False)
    _check_rotation_func(func, 'waterbottle', 'aterbottlew', True)


if __name__ == '__main__':
    _test_rotation_all(is_rotation)
    print 'SUCCESS'




