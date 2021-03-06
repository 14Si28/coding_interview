"""
Implement an algorithm to find the nth to last element of a singly linked list.
"""

import linkedlist # Relative import makes it possible to run this script from any dir, but violates PEP-8.

def find(the_list, nth_from_last):
    """
    Track up to nth_from_last nodes. This is not space efficient.

    the_list: a LinkedList of LinkedListNodes

    nth_from_last: n to last element to return. 0 returns the last node in the list, 1 returns second to last, etc.
    """
    if nth_from_last < 0:
        raise ValueError('Invalid nth from last: {}'.format(nth_from_last))
    current = the_list.head
    visited_nodes = []
    while current:
        if len(visited_nodes) > nth_from_last and len(visited_nodes) > 0:
            visited_nodes.pop(0)
        visited_nodes.append(current)
        current = current.next
    if len(visited_nodes) < nth_from_last:
        raise Exception('The nth from last index exceeds the length of the list: {} > {}'.format(
            nth_from_last, len(visited_nodes)))
    if not visited_nodes:
        raise Exception('List is empty.')
    return visited_nodes.pop(0)

def find_from_end2(the_list, nth_from_end):
    """
    node: the starting Node in the linked list
    """
    start_node = the_list.head
    node = start_node
    seen_count = 0
    found_node = None
    while node:
        if seen_count >= nth_from_end:
            if not found_node:
                found_node = start_node
            else:
                found_node = found_node.next

        seen_count += 1
        node = node.next

    return found_node

#################################
# Tests
#


def _check_func(func, input_list, n, expected_value):
    input_linkedlist = _create_linkedlist(input_list)
    expected = linkedlist.LinkedListNode(expected_value)
    actual = func(input_linkedlist, n)
    if actual != expected:
        raise AssertionError(
            'FAIL: Expected: {}   Actual: {}   Input: {}   n: {}'.format(expected, actual, input_list, n))

def _check_func_calc_expected(func, input_list, n, expected_value=None):
    assert n >= 0
    index = -1 * (n+1)
    if abs(index) > len(input_list):
        raise ValueError('Index out of range. Index: {}  n: {}'.format(index, n))
    expected = input_list[index]
    if expected_value:
        assert expected_value == expected
    _check_func(func, input_list, n, expected)

def _create_linkedlist(pylist):
    test_list = linkedlist.create_linkedlist(pylist)
    assert str(test_list) == str(pylist)
    return test_list

def _test_find_cases(func):
    _check_func(func, [0], 0, 0)
    _check_func(func, [0, 1], 0, 1)
    _check_func(func, [0, 1], 1, 0)
    nine_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    _check_func(func, nine_list, 0, 8)
    _check_func(func, nine_list, 3, 5)
    _check_func_calc_expected(func, nine_list, 3, 5)
    _check_func_calc_expected(func, nine_list, 8, 0)
    _check_func_calc_expected(func, nine_list, 8)
    for x in xrange(len(nine_list)):
        _check_func_calc_expected(func, nine_list, x)

def _test_all():
    _test_find_cases(find)
    _test_find_cases(find_from_end2)
    print 'SUCCESS'

if __name__ == '__main__':
    _test_all()



