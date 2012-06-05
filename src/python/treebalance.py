"""
Convert a sorted array to a balanced binary search tree (BST).
The array is sorted in ascending order.
"""

# We represent nodes as lists: [value, left, right]

def create_bst(values):
    """
    O(n) time complexity.
    """
    if not values:
        return None

    def _bst(start, end):
        if start > end:
            # leaf
            return None

        pivot_index = start + (end - start) / 2
        node = [values[pivot_index], None, None] # value
        node[1] = _bst(start, pivot_index-1) # left
        node[2] = _bst(pivot_index+1, end) # right
        return node

    return _bst(0, len(values)-1)

def is_balanced(tree, threshold=1):
    """
    O(n) time, O(log n) space.
    """
    IMBALANCED = -1
    def height(node):
        if not node:
            return 0
        left_height = height(node[1]) # left
        if left_height == IMBALANCED:
            return IMBALANCED

        right_height = height(node[2]) # right
        if right_height == IMBALANCED:
            return IMBALANCED

        if abs(left_height - right_height) > threshold:
            return IMBALANCED

        return max(left_height, right_height) + 1

    return height(tree) != IMBALANCED


#############################################


# nodes are [value, left, right]
TREE1 = [6, 
            [3, 
                None, 
                [5, None, None]
            ], 
            [8, 
                None, 
                [10, None, None]
            ]
        ]

TREE2 = [8, 
            [5, 
                [3, None, None], 
                [6, None, None]
            ],
            [12, 
                [10, None, None], 
                [15, None, None]
            ]
        ]

def _flatten(tree):
    if not tree:
        return []

    result = []

    def _traverse(node):
        if not node:
            return

        result.append(node[0]) # value
        _traverse(node[1]) # left
        _traverse(node[2]) # right

    _traverse(tree)

    return result

def _test_one(func, expected_tree):
    tree_list = _flatten(expected_tree)
    tree_list.sort()
    actual = func(tree_list)
    if actual != expected_tree:
        raise Exception('FAIL Expected: {}   Actual: {} '.format(expected_tree, actual))
    if not is_balanced(actual):
        raise Exception('FAIL Imbalanced.   Actual: {} '.format(actual))

def _test_all(func):
    _test_one(func, TREE2)
    _test_one(func, TREE1)

def _test_is_balanced():
    assert is_balanced(TREE1)
    assert is_balanced(TREE2)
    assert not is_balanced(
        [ 8, 
            [5, 
                [3, None, None], 
                [6, 
                    None, 
                    [7, None, None]
                ]
            ],
            [10, None, None]
       ])

if __name__ == '__main__':
    _test_is_balanced()
    _test_all(create_bst)

