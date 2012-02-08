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
        if not other or not other.data:
            return 1 # self > other  (other=None is "smaller")
        if not self.data:
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
                s += ','
            s += '{}'.format(x)
        s += ']'
        return s
