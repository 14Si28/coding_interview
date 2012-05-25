"""
Create functions to serialize a binary tree to a string and deserialize it from a string.
"""
import re

TREE_ITEMS_RE = re.compile(r'\s+')
        
def itemize(treestr):
    if not isinstance(treestr, basestring):
        raise ValueError('Tree must be a string: {}'.format(treestr))
    # TODO Error handling, esp. invalid tokens
    items = re.split(TREE_ITEMS_RE, treestr)
    return [x for x in items if x]
    
def _new_node():
    return [None, None, None]

def deserialize(treestr):
    prev = None
    stack = []
    assignments = []
    items = itemize(treestr)
    assert items
    for item in items:
        assert item
        if item == '(':
            stack.append(_new_node())
            assignments.append(_new_node())
        elif item == ')':
            assert stack
            prev = stack.pop()
            assignments.pop()
            if stack:
                top = stack[-1]
                if not assignments[-1][0]:
                    top[0] = prev  # left
                    assignments[-1][0] = True
                else:
                    top[2] = prev  # right
            else:
                # TODO Assert no more items
                break
        else:
            assert stack
            top = stack[-1]
            top[1] = int(item)  # value
            assignments[-1][0] = True

    assert prev
    return prev

def serialize(node):
    if not node:
        return ''
    return ' ( {} {} {} ) '.format(
        serialize(node[0]),  # left
        node[1], # value
        serialize(node[2])  # right
    )

# Using a node class just makes this solution clunkier. We use lists of lists.
# class Node(object):
#     def __init__(self, left=None, value=None, right=None):
#         self.left = left
#         self.value = value
#         self.right = right

def _test_one(serialize_func, deserialize_func, input_tree):
    actual1 = serialize_func(input_tree)
    actual2 = deserialize_func(actual1)
    print '{}  ===>  {}   ===> {}'.format(input_tree, actual1, actual2)
    if actual2 != input_tree:
        raise Exception('FAIL  Expected: {}   Actual (serialized): {}   Actual (deserialized): {}'.format(input_tree, actual1, actual2))

def _test_all(serialize_func, deserialize_func):
    _test_one(serialize_func, deserialize_func, [None, 8, None])
    _test_one(serialize_func, deserialize_func, [[None, 5, None], 8, None])
    _test_one(serialize_func, deserialize_func, [None, 8, [None, 10, None]])
    _test_one(serialize_func, deserialize_func, [[None, 5, None], 8, [None, 10, None]])
    _test_one(serialize_func, deserialize_func, [[None, 5, [None, 7, None]], 8, [None, 10, None]])

if __name__ == '__main__':
    _test_all(serialize, deserialize)

