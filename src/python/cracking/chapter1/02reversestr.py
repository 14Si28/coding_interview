"""
Write code to reverse a C-Style String.

Variant: don't "cheat."
"""

def reverse(s):
    return s[::-1]

# Don't ever do this in python.
def reverse_no_cheating(s):
    r = []
    for x in s:
        r.insert(0, x)
    return ''.join(r)

# Don't ever do this in python.
def reverse_no_cheating_prealloc_array(s):
    import array # Import should be at top. Not following PEP-8 here.
    r = array.array('c', (' ',)*len(s)) # 'c: char array, ('',) tuple for init each elem, *len(s): make it the same size
    for si in xrange(len(s)):
        ri = len(s) - si - 1
        r[ri] = s[si]
    return ''.join(r)

# Don't ever do this in python.
def reverse_no_cheating_in_place(s):
    s = [c for c in s] # Strings in python are immutable. Convert it to an array and pretend we're still doing it "in place".
    for si in xrange(len(s)/2):
        ri = len(s) - si - 1
        swap = s[si]
        s[si] = s[ri]
        s[ri] = swap
    return ''.join(s)

#################################
# Tests
#

def _test_reverse(func, s, expected):
    actual = func(s)
    if actual != expected:
        raise AssertionError('FAIL: Expected: {}   Actual: {}'.format(expected, actual))

def _test_reverse_all(func):
    _test_reverse(func, '', '')
    _test_reverse(func, 'a', 'a')
    _test_reverse(func, 'ab', 'ba')
    _test_reverse(func, 'abc', 'cba')
    _test_reverse(func, 'abcd', 'dcba')
    _test_reverse(func, 'abcdefghi', 'ihgfedcba')

if __name__ == '__main__':
    _test_reverse_all(reverse)
    _test_reverse_all(reverse_no_cheating)
    _test_reverse_all(reverse_no_cheating_prealloc_array)
    _test_reverse_all(reverse_no_cheating_in_place)
    print 'SUCCESS'
