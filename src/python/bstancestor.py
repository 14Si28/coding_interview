"""
Given a binary search tree with integer values sorted from lowest to highest (left nodes lower than right nodes), with no duplicates,
find the lowest level common ancestor of two target values.
"""

def find_ancestor(tree, low_value, high_value):
    """
    O(log n)

    tree: nested tuples of the form (int_value, left_node, right_node)
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

def _test_bst(tree, low, high, expected):
    actual = find_ancestor( tree, low, high )
    print '{} , {} , {}  ===>  {}'.format(tree, low, high, actual)
    if actual != expected:
        raise Exception('FAIL Expected: {}   Actual: {}'.format(expected, actual))
    
def _test_all():
    tree1 = (4, (2, (1, None, None), (3, None, None)), (5, None, None))
    _test_bst( tree1, 1, 5, 4)
    _test_bst( tree1, 1, 3, 2)

    tree2 = (8, 
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
    _test_bst( tree2, 3, 7, 3 )
    _test_bst( tree2, 1, 7, 3 )
    _test_bst( tree2, 3, 13, 8 )
    _test_bst( tree2, 9, 13, 10 )
    _test_bst( tree2, 9, 11, 10 )
    _test_bst( tree2, 11, 13, 12 )

if __name__ == '__main__':
    _test_all()
    
