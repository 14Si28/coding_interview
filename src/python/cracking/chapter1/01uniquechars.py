"""
Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?
"""

# O(n)
def is_unique_via_set(s):
    seen = set()
    for x in s:
        if x in seen:
            return False
        seen.add(x)
    return True

# Gross. Variant of "Check every char of the string with every other char of the string for duplicate occurrences."
def is_unique_via_substr(s):
    for n in xrange(len(s)):
        c = s[n]
        if n > 0 and c in s[0:n-1] or c in s[n+1:]:
            return False
    return True


# NOTE: Alternate solutions:
# Assume charset is ASCII and use a bit vector, O(n).
# Sort and check neighbors, O(n log n).

########################################
# Tests
#

def _check_is_unique(func, s, expected):
    actual = func(s)
    if actual != expected:
        raise AssertionError('FAIL: Expected: {}   Actual: {}   Input: {}    Func: {}'.format(expected, actual, s, func))

def _test_is_unique_chars(func):
    _check_is_unique(func, 'abcdef', True)
    _check_is_unique(func, 'abcdefc', False)
    _check_is_unique(func, 'cabcdef', False)
    _check_is_unique(func, 'abcdcef', False)
    _check_is_unique(func, 'abccdef', False)
    _check_is_unique(func, '', True)
    _check_is_unique(func, 'a', True)
    _check_is_unique(func, 'aaaaaaaaaaa', False)

if __name__ == '__main__':
    _test_is_unique_chars(is_unique_via_set)
    _test_is_unique_chars(is_unique_via_substr)
    print 'SUCCESS'

