"""
Illustrate a breadth first search in a binary tree.
"""

# One solution is to model a tree with classes, roughly:
# class TreeNode(object): left=None; right=None;  class Tree(object): root = TreeNode()
#
# It's easier to express trees in python as lists of lists, where each node is:
# [ left, right, value ]
#
# Great example here: http://code.activestate.com/recipes/577540-python-binary-search-tree/

LEFT_NODE_INDEX = 0
RIGHT_NODE_INDEX = 1
VALUE_INDEX = 2

def bfs(tree, value_to_find):
    """
    Breadth first search.
    
    tree: list of lists representing a tree, of the form [ left, right, value ],
        e.g. [ [None, None, 2], [None, None, 3], 1 ]

    value: the value to search for.
    """
    found_node = None
    route = ''

    to_visit = [tree]
    while to_visit:
        node = to_visit.pop(0)
        value = node[VALUE_INDEX]
        route += str(value)
        if value == value_to_find:
            found_node = node
            break
        to_visit.append(node[LEFT_NODE_INDEX])
        to_visit.append(node[RIGHT_NODE_INDEX])

    return found_node, route



#################################
# Tests
#

#def _check_bfs_func(func, s1, s2, expected):
#    actual = func(s1, s2)
#    if actual != expected:
#        raise AssertionError(
#            'FAIL: Expected: {}   Actual: {}   Input s1: {}   s2: {}'.format(expected, actual, s1, s2))

def _test_bfs_all(func):
    # TODO Proper tests
    #_check_bfs_func(func, '', '', True)
    t = func([ [None, None, 2], [None, None, 3], 1 ], 3)
    assert t[0][VALUE_INDEX] == 3
    assert t[1] == '123'
    print t
    t = func([ [ [None, None, 4], [ None, None, 5], 2], [ [ None, None, 6], [ None, None, 7], 3], 1 ], 7)
    assert t[0][VALUE_INDEX] == 7
    assert t[1] == '1234567'
    print t


if __name__ == '__main__':
    _test_bfs_all(bfs)
    print 'SUCCESS'




