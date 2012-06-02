"""
Implement a function to check if a tree is balanced For the purposes of this question, a balanced tree is defined to be a 
tree such that no two leaf nodes differ in distance from the root by more than one.
"""


def is_balanced2(tree, threshold=1):
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


def is_balanced(tree, threshold=1):
    """
    O(n^2) time.
    """
    if not tree:
        return True

    def height(node):
        if not node:
            return 0

        return 1 + max(height(node[1]), height(node[2]))

    return abs(height(tree[1]) - height(tree[2])) <= threshold


def _test_all(func):
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
    assert func(tree2)
    tree1 = (8, 
                (3, None, None), 
                (10, (9, None, None), 
                    (12, 
                        (11, None, None), 
                        (13, None, None)
                    )
                )
            )
    assert not func(tree1)

if __name__ == '__main__':
    _test_all(is_balanced2)
    _test_all(is_balanced)

