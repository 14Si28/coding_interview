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

## Illustration. Don't do this in python.
#def ExampleNode(object):
#    def __init__(self, data, previous=None, next=None):
#        self.previous = previous
#        self.next = next
#        self.data = data
#
## Illustration. Don't do this in python.
#def ExampleList(object):
#    def __init__(self, head):
#        self.head = head
#
#    def traverse(locate_node=None):
#        pass
#
#    def append(node):
#        pass

#################################
# Tests
#


def _check_func(func, input_nodes, expected):
    actual = func(input_nodes)
    if actual != expected:
        raise AssertionError(
            'FAIL: Expected: {}   Actual: {}   Input: {}'.format(expected, actual, input_nodes))

def _test_all(func):
    _check_func(func, [], [])
    _check_func(func, [0], [0])
    _check_func(func, [0,1], [0,1])
    _check_func(func, [0,0,1], [0,1])
    _check_func(func, [0,1,1], [0,1])
    _check_func(func, [0,1,1,2,3,3,4,5,5,5,6,7,8,8,8], [0,1,2,3,4,5,6,7,8])
    #_check_func(func, [1,0,1,1], [1,0]) # Expected ordering depends on func removing first or remaining duplicates.

if __name__ == '__main__':
    _test_all(remove_duplicates)
    _test_all(remove_duplicates_no_temp)
    print 'SUCCESS'


