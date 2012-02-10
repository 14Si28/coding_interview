"""
Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node.
EXAMPLE
Input: the node 'c' from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a->b->d->e
"""

import linkedlist

def delete_node(node):
    """
    node: LinkedListNode
    """
    if not node.next:
        raise Exception('Cannot delete last node in list.')
    node.data = node.next.data
    node.next = node.next.next


#################################
# Tests
#

if __name__ == '__main__':
    test_list = linkedlist.create_linkedlist([0, 1, 2])
    node = test_list.head.next
    assert node.data == 1
    delete_node(node)
    assert str(test_list) == '[0, 2]'
    print 'SUCCESS'


