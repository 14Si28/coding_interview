"""
Reverse a singly linked list.

The singly linked list does not have a "previous" pointer as would be seen with a doubly linked list.
"""

import linkedlist

def reverse(input_list):
    """
    input_list: a linkedlist.LinkedList
    """
    if input_list.head == input_list.last:
        return input_list

    prev = input_list.head
    curr = input_list.head.next
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    input_list.head.next = None
    input_list.last = input_list.head
    input_list.head = prev

    return input_list

def _test(func, input):
    expected = input[::-1]
    input_str = str(input)
    input = linkedlist.create_linkedlist(input)
    actual = func(input)
    print '{}    ====>   {}'.format(input_str, actual)
    if str(actual) != str(expected):
        raise Exception('FAIL Expected: {}   Actual:  {}'.format(expected, actual))

def _test_all(func):
    _test(func, [0,1,2,3])
    _test(func, [0,1,2,3,4,5,6,7])
    _test(func, [0,1])
    _test(func, [0])
    print 'SUCCESS'

if __name__ == '__main__':
    _test_all(reverse)
