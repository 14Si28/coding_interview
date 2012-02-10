"""
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
Output: 8 -> 0 -> 8

Alternate solution: recursive impl.
"""

import linkedlist

def add_list_numbers(left, right):
    """
    left: LinkedList with the int in each node representing digits in a number, least significant digit first. e.g. 3 -> 1 -> 5 = 513
    right: LinkedList similarly represented. e.g. 5 -> 9 -> 2 = 295

    returns: LinkedList similarly represented, the sum of left and right. e.g. 808
    """
    left_int = _list_to_int(left)
    right_int = _list_to_int(right)
    return _int_to_list(left_int + right_int)

def _list_to_int(the_list):
    result = 0
    multiple = 1
    for node in the_list.traverse_nodes():
        result += node.data * multiple
        multiple *= 10
    return result

def _int_to_list(the_int):
    if not the_int:
        return linkedlist.create_linkedlist([0])
    else:
        result = []
        remaining_int = the_int
        while remaining_int != 0:
            digit = remaining_int % 10
            result.append(digit)
            remaining_int = int(remaining_int/10)
    return linkedlist.create_linkedlist(result)


#################################
# Tests
#


def _check_func(func, left, right, expected):
    left_list = linkedlist.create_linkedlist(left)
    right_list = linkedlist.create_linkedlist(right)
    expected_list = linkedlist.create_linkedlist(expected)
    actual = func(left_list, right_list)
#    print '{} == {}'.format(actual, expected_list)
    if str(actual) != str(expected_list):
        raise AssertionError(
            'FAIL: Expected: {}   Actual: {}   Input left: {}  Input right: {}'.format(
                expected_list, actual, left, right))

def _test_add_cases(func):
    _check_func(func, [3, 1, 5], [5, 9, 2], [8, 0, 8])
    _check_func(func, [1, 2, 3], [4, 5, 6], [5, 7, 9])
    _check_func(func, [1], [1], [2])
    _check_func(func, [1], [0], [1])
    _check_func(func, [1], [2], [3])
    _check_func(func, [0], [0], [0])
    _check_func(func, [0, 1], [2], [2, 1])
    _check_func(func, [0, 0, 1], [2], [2, 0, 1])

def _test_all():
    _test_add_cases(add_list_numbers)
    print 'SUCCESS'

if __name__ == '__main__':
    _test_all()



