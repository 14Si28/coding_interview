"""
Find the nth value from the end of a singly linked list.
"""

class Node(object):
    def __init__(self, value=None, next=None):
        self.next = next
        self.value = value

    def __str__(self):
        return '(Node: {})'.format(self.value)

def find_from_end2(node, nth_from_end):
    """
    node: the starting Node in the linked list
    """
    start_node = node
    seen_count = 1
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

def find_from_end(values, nth_from_end):
    """
    values: list of values
    """
    nth_index = -1 * nth_from_end 
    for i in xrange(len(values)):
        nth_index += 1

    return values[nth_index]


############################


def to_linkedlist(values):
    start = Node(value=values[0])
    prev = start
    for v in values[1:]:
        new_node = Node(value=v)    
        prev.next = new_node
        prev = prev.next
    return start

def node_value(node):
    return getattr(node, 'value', None)

def _test_one(func, values, nth_from_end, expected, input_adapter, output_adapter):
    if input_adapter:
        values = input_adapter(values)

    actual = func(values, nth_from_end)

    if output_adapter:
        actual = output_adapter(actual)

    print '{}  {} , {} ==> {}'.format(func, values, nth_from_end, actual)
    if actual != expected:
        raise Exception('FAIL: expected: {}  actual: {}'.format(expected, actual))

def _test_all(func, input_adapter=None, output_adapter=None):
    _test_one(func, [0,1,2,3,4,5,6,7], 3, 5, input_adapter, output_adapter)

if __name__ == '__main__':
    _test_all(find_from_end)
    _test_all(find_from_end2, input_adapter=to_linkedlist, output_adapter=node_value)

