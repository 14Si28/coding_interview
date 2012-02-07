"""
Write a method to replace all spaces in a string with %20.
"""

def replace_spaces_cheat(s):
    return s.replace(' ', '%20')

# Illustrates an algorithm. Don't ever do this in python.
def replace_spaces_array(s):
    # If you MUST use primitive arrays and indexes, and cannot use array's insert...
    orig_arr  = [c for c in s]
    spaces_count = len([c for c in s if c == ' '])
    new_space = '%20'
    import array # Import should be at top. Not following PEP-8 here so we colocate the ugly import of array.
    new_len = len(s) + spaces_count*(len(new_space)-1) # len(s) counts the existing spaces once, new spaces size = (3 - 1)
    new_arr  = array.array('c', (' ',)*new_len) # 'c: char array, ('',) tuple for init each elem, * len: make it the same size

    new_index = 0
    for c in orig_arr:
        if c == ' ':
            for space_char in new_space:
                new_arr[new_index] = space_char
                new_index += 1
        else:
            new_arr[new_index] = c
            new_index += 1

    return ''.join(new_arr)

#################################
# Tests
#

def _check_spaces_func(func, s, expected):
    actual = func(s)
    if actual != expected:
        raise AssertionError(
            'FAIL: Expected: {}   Actual: {}   Input: {}'.format(expected, actual, s))

def _test_spaces_all(func):
    _check_spaces_func(func, 'hello world', 'hello%20world')
    _check_spaces_func(func, 'this has spaces', 'this%20has%20spaces')
    _check_spaces_func(func, ' space at beginning', '%20space%20at%20beginning')
    _check_spaces_func(func, 'space at end ', 'space%20at%20end%20')
    _check_spaces_func(func, '   ', '%20%20%20')
    _check_spaces_func(func, ' ', '%20')
    _check_spaces_func(func, '', '')
    _check_spaces_func(func, 'abc', 'abc')

if __name__ == '__main__':
    _test_spaces_all(replace_spaces_cheat)
    _test_spaces_all(replace_spaces_array)
    print 'SUCCESS'




