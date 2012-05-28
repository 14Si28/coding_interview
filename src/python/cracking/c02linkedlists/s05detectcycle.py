"""
Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
EXAMPLE
input: A -> B -> C -> D -> E -> C [the same C as earlier]
output: C
"""

import linkedlist

def find_cycle_node(the_list):
    """
    Detect cycles by tracking the id of every visited node.
    Average O(n) time, O(n) space.

    the_list: a LinkedList of LinkedListNodes

    returns: first node in the loop.
    """
    seen = set()
    node = None
    for node in the_list.traverse_nodes():
        if id(node) in seen:
            break
        seen.add(id(node))
    return node

def find_cycle_node_skip(the_list):
    """
    Detect cycles using Floyd's algorithm (aka skip pointer, fast, runner, hare).
    Average case O(n) time (actually O(lambda + mu), see wiki)
    Space O(1)

    http://en.wikipedia.org/wiki/Cycle_detection

    the_list: a LinkedList of LinkedListNodes

    returns: first node in the loop.
    """

    def skip(node):
        if node and node.next:
            return node.next.next
        return None

    fast_node = skip(the_list.head)
    slow_node = the_list.head.next
    while slow_node and id(fast_node) != id(slow_node):
        fast_node = skip(fast_node)
        slow_node = slow_node.next

    if not fast_node:
        return None

    slow_node = the_list.head
    while id(slow_node) != id(fast_node):
        slow_node = slow_node.next
        fast_node = fast_node.next

    return fast_node


#################################
# Tests
#

def _check_func(func, the_list, expected):
    actual = func(the_list)
    if actual != expected:
        raise AssertionError(
            'FAIL: Expected: {}   Actual: {}'.format(expected, actual))

def _test_cycle(func, pylist, start_val, end_val):
    the_list = linkedlist.create_linkedlist(pylist)
    # Create a cycle.
    start = the_list.find_node(start_val)
    end = the_list.find_node(end_val)
    end.next = start
    _check_func(func, the_list, start)

def _test_cycle_cases(func):
    _test_cycle(func, [0, 1, 2, 3, 4, 5], 0, 3)
    _test_cycle(func, [0, 1, 2, 3, 4, 5], 1, 4)
    _test_cycle(func, [0, 1, 2, 3, 4, 5], 2, 5)

def _test_all():
    _test_cycle_cases(find_cycle_node)
    _test_cycle_cases(find_cycle_node_skip)
    print 'SUCCESS'

if __name__ == '__main__':
    _test_all()




