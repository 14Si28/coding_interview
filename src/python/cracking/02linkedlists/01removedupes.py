"""
Part 1: Write code to remove duplicates from an unsorted linked list.
Part 2: How would you solve this problem if a temporary buffer is not allowed?
"""

def remove_duplicates(nodes):
    """
    An inefficient but clear removal of duplicates that triples the reference count of the nodes.

    nodes: a list of objects. Their __hash__, __cmp__ or __eq__ (if defined) will be used to determine equality.
    """
    # If order is unimportant, can do this in a single line:
    # return [x for x in set(nodes)]
    seen = set()
    result = []
    for x in nodes:
        if not x in seen:
            result.append(x)
            seen.add(x)
    return result

# Illustrates an algorithm. Don't ever do this in python.
def remove_duplicates_no_temp(nodes):
    """
    Avoid using any temporary storage (no sets).
    Repeatedly scan the entire list for duplicates of the current node.
    Remove duplicates from the original list in place, removing the first (not last) of each duplicate.

    nodes: a list of objects. Their __cmp__ or __eq__ (if defined) will be used to determine equality.
    """
    index_offset = 0
    original_len = len(nodes)
    for index in xrange(original_len):
        for scan_index in xrange(index+1, original_len):
            if nodes[index-index_offset] == nodes[scan_index-index_offset]:
                nodes.pop(index-index_offset)
                index_offset += 1
                break
    return nodes



# Illustration. Don't do this in python. Normally just use built in lists.
class SillyNode(object):
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


# Illustration. Don't do this in python. Normally just use built in lists.
class SillyList(object):
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

    def remove_duplicates(self):
        """
        Remove duplicates in place by repeatedly scanning the list for duplicates.
        """
        if not self.head:
            return
        current = self.head.next
        previous = self.head
        while current:
            scanner = current.next
            current_removed = False
            while scanner:
                if scanner == current:
                    # Remove duplicate at current (former) and keep scanner (latter)
                    previous.next = current.next
                    current = previous.next
                    current_removed = True
                    break
                scanner = scanner.next
            if not current_removed:
                previous = current
                current = current.next


#################################
# Tests
#


def _check_func(func, input_nodes, expected):
    actual = func(input_nodes)
    if actual != expected:
        raise AssertionError(
            'FAIL: Expected: {}   Actual: {}   Input: {}'.format(expected, actual, input_nodes))

def _test_silly_list():
    silly_list = SillyList(SillyNode(0))
    silly_list.append(SillyNode(1))
    silly_list.append(SillyNode(1))
    silly_list.append(SillyNode(2))
    silly_list.append(SillyNode(3))
    silly_list.append(SillyNode(3))
    silly_list.append(SillyNode(1))
#    print silly_list
    assert silly_list.__str__() == '[0,1,1,2,3,3,1]'
    silly_list.remove_duplicates()
#    print silly_list
    assert silly_list.__str__() == '[0,2,3,1]'


def _test_all(func):
    _check_func(func, [], [])
    _check_func(func, [0], [0])
    _check_func(func, [0,1], [0,1])
    _check_func(func, [0,0,1], [0,1])
    _check_func(func, [0,1,1], [0,1])
    _check_func(func, [0,1,1,2,3,3,4,5,5,5,6,7,8,8,8], [0,1,2,3,4,5,6,7,8])
    #_check_func(func, [1,0,1,1], [1,0]) # Expected ordering depends on whether func removes former or latter duplicates.

if __name__ == '__main__':
    _test_all(remove_duplicates)
    _test_all(remove_duplicates_no_temp)
    _test_silly_list()
    print 'SUCCESS'


