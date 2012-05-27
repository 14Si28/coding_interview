"""
You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes.
Create an algorithm to decide if T2 is a subtree of T1.
T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
"""

def subtree(tree1, tree2):
	"""
	returns: True if tree2 is a subtree of tree1
	"""
	if not tree2:
		return True

	def all_nodes_match(node1, node2):
		if not node1 and not node2:
			return True # Nothing left in subtree
		if not node1 or not node2:
			return False
		if node1[0] != node2[0]:
			# Values do not match
			return False
		return ( all_nodes_match(node1[1], node2[1]) # left
			and all_nodes_match(node1[2], node2[2]) ) # right

	def subtree_recurse(node1, node2):
		if not node1 or not node2:
			return False
		if node1[0] == node2[0]:
			return all_nodes_match(node1, node2)
		return ( subtree_recurse(node1[1], node2) # left
			or subtree_recurse(node1[2], node2) ) # right

	return subtree_recurse(tree1, tree2)

def _test_all():
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
	tree1 = (3, (1, None, None), 
                    (6, 
                        (4, None, None), 
                        (7, None, None)
                    )
                )
	tree3 = (1, None, None)
	assert subtree(tree2, tree1)
	assert subtree(tree2, tree2)
	assert subtree(tree1, tree1)
	assert not subtree(tree1, tree2)
	assert subtree(tree1, tree3)
	assert subtree(tree2, tree3)
	assert not subtree(tree3, tree2)

if __name__ == '__main__':
	_test_all()

	
