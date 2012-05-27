"""
Given a binary search tree with integer values sorted from lowest to highest (left nodes lower than right nodes), with no duplicates,
find the lowest level common ancestor of two target values.
"""

def find_ancestor_bst(tree, low_value, high_value):
    """
    O(log n)

    tree: nested tuples of the form (int_value, left_node, right_node). MUST be a binary search tree (sorted).
    low_value: smaller int 
    high_value: larger int

    returns: int value of smallest (lowest level) common ancestor
    """
    assert low_value < high_value
    # Assume sorted BST, lowest to highest, no duplicates.
    node = tree
    while node:
        current_value = node[0]
        if current_value < low_value:
            node = node[2] # go right to higher values
        elif current_value > high_value:
            node = node[1] # go left to lower values
        elif low_value <= current_value <= high_value:
            return current_value
        else:
            break
    return None

def find_ancestor_bintree(node, p_node, q_node):
    """
    node: a binary tree (not a BST, may not be sorted).
    p_node, q_node: nodes to find ancestor of.

    returns: tuple of (common_ancestor_node, true_if_ancestor)
        true_if_ancestor distinguishes a real common ancestor from node not found.
        true_if_ancestor is only True if both p_node and q_node were found.
    """
    if not node:
        return None, False

    if node == p_node == q_node:
        return node, True

    print ' ?? {} '.format(node)
    x, rx = find_ancestor_bintree(node[1], p_node, q_node) # left
    if x and x != p_node and x != q_node:
        return x, rx

    y, ry = find_ancestor_bintree(node[2], p_node, q_node) # right
    if y and y != p_node and y != q_node:
        return y, ry

    if x and y:
        # Found the comon ancestor
        return node, True
    elif node == p_node or node == q_node:
        # If at one of the nodes to find (p_node or q_node), 
        # and we also found the other node in a subtree (x or y)
        # then this node is really the ancestor. 
        # Otherwise one of the target values has not been found,
        # and this is not a true ancestor.
        real_ancestor = x or y
        return node, real_ancestor
    else:
        assert not x or not y
        a = x if x else y
        return a, False

def _test_bst(func, tree, low, high, expected):
    actual = func( tree, low, high )
    print '{} , {} , {}  ===>  {}'.format(tree, low, high, actual)
    if actual != expected:
        raise Exception('FAIL Expected: {}   Actual: {}'.format(expected, actual))
    
def create_tree2():
    return (8, 
                (3, (1, None, None), 
                    (6, 
                        (4, None, None), 
                        (7, None, None)
                    )
                ), 
                (10, (9, None, None), 
                    (12, 
                        (11, None, None), 
                        (13, None, None)
                    )
                )
            )

def _test_all(func):
    tree1 = (4, (2, (1, None, None), (3, None, None)), (5, None, None))
    _test_bst(func, tree1, 1, 5, 4)
    _test_bst(func, tree1, 1, 3, 2)

    tree2 = create_tree2()
    _test_bst(func, tree2, 3, 7, 3 )
    _test_bst(func, tree2, 1, 7, 3 )
    _test_bst(func, tree2, 3, 13, 8 )
    _test_bst(func, tree2, 9, 13, 10 )
    _test_bst(func, tree2, 9, 11, 10 )
    _test_bst(func, tree2, 11, 13, 12 )

def _test_find_ancestor_bintree():
    tree2 = create_tree2()
    p_node = tree2[1][2][1]
    q_node = tree2[1][1]
    actual, real_ancestor = find_ancestor_bintree(tree2, p_node, q_node)
    print '! {}'.format(actual)
    assert actual == tree2[1]
    assert real_ancestor

if __name__ == '__main__':
    _test_all(find_ancestor_bst)
    _test_find_ancestor_bintree()

