"""
Write a method to decide if two strings are anagrams or not.

An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; for example orchestra can be rearranged into carthorse. 
"""

def is_anagram_cheat(a, b):
    """
    Convert strings to lists, sort them, convert back, compare. The conversions make this ugly.
    """
    if a == b: # it's not an anagram if it's identical
        return False
    return sorted(a) == sorted(b)

def is_anagram_naive(a, b):
    """
    Illustrate an actual algorithm.
    Naive anagram check. O(n), wasted storage for counts, worst case 3x iterations.
    """
    if a == b:
        return False
    if len(a) != len(b):
        return False

    a_count = {}
    for c in a:
        a_count.setdefault(c, 0)
        a_count[c] += 1
    b_count = {}
    for c in b:
        b_count.setdefault(c, 0)
        b_count[c] += 1

    for k,v in a_count.iteritems():
        if not k in b_count or b_count[k] != v:
            return False
    return True


#################################
# Tests
#

def _check_anagram_func(func, a, b, expected):
    actual = func(a, b)
    if actual != expected:
        raise AssertionError(
            'FAIL: Expected: {}   Actual: {}   Input a: {}  Input b: {}'.format(expected, actual, a, b))

def _test_anagram_all(func):
    _check_anagram_func(func, '', '', False)
    _check_anagram_func(func, 'a', 'b', False)
    _check_anagram_func(func, 'ab', 'ba', True)
    _check_anagram_func(func, 'abb', 'bab', True)
    _check_anagram_func(func, 'abba', 'baba', True)
    _check_anagram_func(func, 'catalogue', 'coagulate', True)
    _check_anagram_func(func, 'basiparachromatin', 'marsipobranchiata', True)
    _check_anagram_func(func, 'undefinability', 'unidentifiably', True)
    _check_anagram_func(func, 'undefinability', 'unidentifiable', False)

def _test_all():
    _test_anagram_all(is_anagram_naive)
    _test_anagram_all(is_anagram_cheat)
    print 'SUCCESS'

if __name__ == '__main__':
    _test_all()



