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

    def traverse(self):
        """
        Create an iterator over the list of nodes.
        """
        if not self.head:
            yield None
        else:
            current = self.head
            while current:
                yield current.data
                current = current.next

    def __str__(self):
        s = '['
        for x in self.traverse():
            if len(s) > 1:
                s += ', '
            s += '{}'.format(x)
        s += ']'
        return s


def create_linkedlist(pylist):
    """
    Create a LinkeList of LinkedListNodes from a standard python list.
    """
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