"""
Create functions to serialize a binary tree to a string and deserialize it from a string.
"""
import re

TREE_ITEMS_RE = re.compile(r'\s+')
NONE_STR = str(None)

def serialize_recurse(node):
    """
    Serialize using depth first pre-order traversal, returned strings values are space delimited.
    """
    if not node:
        return NONE_STR

    assert len(node) == 3

    return ' {} {} {} '.format(
        node[1], # value
        serialize_recurse(node[0]), # left
        serialize_recurse(node[2]) # right
    )

def deserialize_recurse(treestr):
    """
    Deserialize from a space delimited tree string using depth first pre-order traversal.
    """
    items = itemize_parens(treestr)

    # A function to use as a namespace to workaround for python 2.x lack of closure scoping, refer to python 3.x nonlocal 
    def f(): pass
    # Track the index in the items outside of the recursive function calls.
    f.index = 0

    def _desr():
        if f.index > len(items) - 1 or items[f.index] == NONE_STR:
            f.index += 1
            return None

        node = _new_node()
        node[1] = int(items[f.index])
        f.index += 1
        node[0] =_desr()
        node[2] =_desr()
        return node

    return _desr()

def serialize_parens(node):
    """
    Create a string version of the tree with parenthesis to group each node, spaces delimit all tokens.

    node: a list of lists representing the tree, each list has 3 elements (left, value, right).

    Examples: 
    [None, 8, None]  ===>   (  8  )
    [[None, 5, None], 8, None]  ===>   (  (  5  )  8  )
    [None, 8, [None, 10, None]]  ===>   (  8  (  10  )  )
    """
    if not node:
        return ''
    return ' ( {} {} {} ) '.format(
        serialize_parens(node[0]),  # left
        node[1], # value
        serialize_parens(node[2])  # right
    )
        
def itemize_parens(treestr):
    if not isinstance(treestr, basestring):
        raise ValueError('Tree must be a string: {}'.format(treestr))
    # TODO Error handling, esp. invalid tokens
    items = re.split(TREE_ITEMS_RE, treestr)
    return [x for x in items if x]
    
def _new_node():
    return [None, None, None]

def deserialize_parens(treestr):
    """
    Deserialize the parenthesis tree string using iteration.
    """
    prev = None
    stack = [] # Place to store nodes as we reconstruct the tree
    assignments = [] # Track whether the left node has been assigned
    items = itemize_parens(treestr)
    assert items
    for item in items:
        assert item
        if item == '(':
            stack.append(_new_node())
            assignments.append(False)
        elif item == ')':
            assert stack
            prev = stack.pop()
            assignments.pop()
            if stack:
                top = stack[-1]
                if not assignments[-1]:
                    top[0] = prev  # left
                    assignments[-1] = True
                else:
                    top[2] = prev  # right
            else:
                # TODO Assert no more items
                break
        else:
            assert stack
            top = stack[-1]
            top[1] = int(item)  # value
            assignments[-1] = True

    assert prev
    return prev

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
    _test_one(serialize_func, deserialize_func, [[None, 5, [None, 7, None]], 8, [[None, 9, None], 10, [None, 11, None]]])

if __name__ == '__main__':
    _test_all(serialize_parens, deserialize_parens)
    _test_all(serialize_recurse, deserialize_recurse)

