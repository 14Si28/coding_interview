"""
Given a binary search tree with integer values sorted from lowest to highest (left nodes lower than right nodes), with no duplicates,
find the lowest level common ancestor of two target values.
"""

def _search(tree, target_value):
    assert len(tree) == 3
    visited = []
    node = list(tree)
    while node:
        current = node
        assert len(node) == 3
        current_value = current[0]
        node = []
        visited.append(current_value)
        if target_value == current_value:
            return visited
        elif target_value < current_value:
            node = current[1] # left
        else:
            assert target_value > current_value 
            node = current[2] # right
    return None # not found

def find_ancestor(tree, low_value, high_value):
    # Assume sorted BST, lowest to highest, no duplicates.
    # Find paths to target values.
    low_path = _search(tree, low_value)
    high_path = _search(tree, high_value)
    # Find the lowest intersection of the paths.
    for high_index in xrange(len(high_path)-1, -1, -1):
        for low_index in xrange(len(low_path)):
            current = low_path[low_index]
            # print '? {} == {} '.format(current, high_path[high_index])
            if current == high_path[high_index]:
                return current
    return None
    

def _test_bst(tree, low, high, expected):
    # (value, left, right)
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
    
