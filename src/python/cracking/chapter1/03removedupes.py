"""
Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer.
NOTE: One or two additional variables are fine. An extra copy of the array is not.
"""

def remove_dupes_cheat(s):
    """
    Removes duplicates quickly but fails to preserve ordering.
    """
    return ''.join(set(s))

# Illustrates an algorithm.
# O(n^2)
def remove_dupes_no_extra_buffer(s):
    s = [c for c in s] # Strings in python are immutable. Convert it to an array and pretend.

    last = 0
    for c in s:
        if not(last > 0 and c in s[0:last]):
            s[last] = c
            last += 1

    return ''.join(s[0:last]) # Convert back to string.

def remove_dupes_via_set(s):
    r = []
    seen = set()
    for c in s:
        if not c in seen:
            r.append(c)
        seen.add(c)
    return ''.join(r)

#################################
# Tests
#

def _check_str_func(func, s, expected):
    actual = func(s)
    if actual != expected:
        raise AssertionError('FAIL: Expected: {}   Actual: {}   Input: {}'.format(expected, actual, s))

def _test_remove_dupes_all(func):
    _check_str_func(func, '', '')
    _check_str_func(func, 'a', 'a')
    _check_str_func(func, 'ab', 'ab')
    _check_str_func(func, 'aa', 'a')
    _check_str_func(func, 'aab', 'ab')
    _check_str_func(func, 'abb', 'ab')
    _check_str_func(func, 'abbc', 'abc')
    _check_str_func(func, 'abbcc', 'abc')
    _check_str_func(func, 'abbccdddd', 'abcd')
    _check_str_func(func, 'abcdabcd', 'abcd')
    _check_str_func(func, 'aaaa12345678907415690248723041893075354123', 'a1234567890')

if __name__ == '__main__':
    _test_remove_dupes_all(remove_dupes_no_extra_buffer)
    _test_remove_dupes_all(remove_dupes_via_set)
    _check_str_func(remove_dupes_cheat, 'abb', 'ab')
    print 'SUCCESS'
