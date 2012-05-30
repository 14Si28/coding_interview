"""
Illustrate binary search on a BST.
"""

# nodes are [value, left, right]
TREE1 = [ 8, 
            [5, 
                [3, None, None], 
                [6, None, None]
            ],
            [10, None, None]
       ]
       
def binarysearch(node, value_to_find):
    """
    node: list of lists representing a BST
    """
    if not node:
        return None
    if node[0] == value_to_find:
        return node
    
    found = binarysearch(node[1], value_to_find) # left
    if not found:
        found = binarysearch(node[2], value_to_find) # right
    return found
    
def _test_all():
    assert binarysearch(TREE1, 3) == [3, None, None]
    assert binarysearch(TREE1, 10) == [10, None, None]
    actual = binarysearch(TREE1, 5)
    assert actual[0] == 5
    print 'SUCCESS'

if __name__ == '__main__':
	_test_all()