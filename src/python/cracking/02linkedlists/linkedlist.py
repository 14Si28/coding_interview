"""
A linked list example implementation. In normal python you would just use the list builtin.
"""

# Illustration. Don't do this in python.
class LinkedListNode(object):
    def __init__(self, data, previous=None, next=None):
        self.previous = previous
        self.next = next
        self.data = data

    def __cmp__(self, other):
        if other == None: # Don't use `if not other`, since then it won't work for 0, [], etc.
            return 1 # self > other  (other=None is "smaller")
        if self.data == None:
            return -1 # self < other
        return self.data.__cmp__(other.data)

    def __hash__(self):
        return self.data.__hash__() # __hash__() is defined for None so we don't need additional checks.

    def __str__(self):
        return '{}'.format(self.data)


# Illustration. Don't do this in python.
class LinkedList(object):
    def __init__(self, head):
        """
        head: SillyNode
        """
        self.head = head
        self.last = head

    def append(self, node):
        """
        node: SillyNode
        """
        self.last.next = node
        self.last = node

    def traverse_data(self):
        """
        Create an iterator over the list's data.
        """
        if not self.head:
            yield None
        else:
            current = self.head
            while current:
                yield current.data
                current = current.next

    def traverse_nodes(self):
        """
        Create an iterator over the list nodes.
        """
        if not self.head:
            yield None
        else:
            current = self.head
            while current:
                yield current
                current = current.next

    def find_nodes(self, node_value, start_node=None):
        """
        returns: a generator over all nodes with node_value, or [] if none found.
        """
        if not start_node:
            start_node = self.head

        started = False
        for node in self.traverse_nodes():
            if node == start_node:
                started = True
            if started and node.data == node_value:
                yield node

    def find_node(self, node_value, start_node=None):
        nodes = list(self.find_nodes(node_value, start_node=start_node))
        if len(nodes) > 0:
            return nodes[0]
        return None

    def __str__(self):
        s = '['
        for x in self.traverse_data():
            if len(s) > 1:
                s += ', '
            s += '{}'.format(x)
        s += ']'
        return s


def create_linkedlist(pylist):
    """
    Create a LinkeList of LinkedListNodes from a standard python list.
    """
    if not pylist:
        raise ValueError('Cannot create empty list.')
    new_list = LinkedList(LinkedListNode(pylist[0]))
    for x in pylist[1:]:
        new_list.append(LinkedListNode(x))
    return new_list




#################################
# Tests
#

def _test_create():
    input = [0, 1, 1, 2, 3, 3, 1]
    test_list = create_linkedlist(input)
    assert str(test_list) == str(input)

def _test_equals():
    a = LinkedListNode(0)
    b = LinkedListNode(0)
    c = LinkedListNode(1)
    assert a == b
    assert a != c
    assert b != c
    assert str(a) == str(b)
    assert str(a) != str(c)

def _test_all():
    _test_create()
    _test_equals()


if __name__ == '__main__':
    _test_all()