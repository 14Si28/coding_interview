"""
Illustrate a skip list search.
"""
import random

# References:
# http://cg.scs.carleton.ca/~morin/teaching/5408/refs/p90b.pdf
# http://en.wikipedia.org/wiki/Skip_list

class Node(object):
    """
    A skip list node.
    """
    MAX_LEVEL = 2   # 0 based
    def __init__(self, value=None, first=False):
        self.value = value
        # level is 0 based
        self.level = self.MAX_LEVEL if first else Node.random_level()
        self.forward = [None,] * (self.level+1)

    def __str__(self):
        return '{}'.format(self.value)

    def __repr__(self):
        return 'Node(value={})'.format(self.value)

    def traverse(self, level=0):
        if self.level < level:
            raise ValueError('The level at this node: {} is less than the level for traversal: {}'.format(self.level, level))

        node = self
        while node:
            assert node.level == len(node.forward) - 1
            yield node
            node = node.forward[level]

    @classmethod
    def random_level(cls):
        # 50% level 0, 25% level 1, 12.5% level 2...
        m = 100
        p = random.randint(1, m)

        level = 0
        m /= 2
        while p < m and level < Node.MAX_LEVEL:
            m /= 2
            level += 1

        return level

def create_base_list(num_nodes):

    first = Node(value=0, first=True)
    # Track the previous node for each level.
    previous_nodes = [first,] * (Node.MAX_LEVEL + 1)

    node = first
    for x in xrange(1, num_nodes):
        node.forward[0] = Node(value=x)
        node = node.forward[0]

        if node.level > 0:
            prev = previous_nodes[node.level]
            if prev:
                # Stitch together nodes with the same level.
                prev.forward[node.level] = node
                #print 'Skip {}  ==> {}   @ level {}'.format(prev, node, node.level)

            previous_nodes[node.level] = node

    return first

def print_list(first_node):
    for level in xrange(0,len(first_node.forward)):
        print '____ Level: {} '.format(level)
        for node in first_node.traverse(level):
            print '{},'.format(node.value),
        print ''
    print ''

def _test_all():
    first_node = create_base_list(100)
    print_list(first_node)

if __name__ == '__main__':
    _test_all()
