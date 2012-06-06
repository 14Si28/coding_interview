"""
Implement a stack.
"""

import unittest

# NOTE: Python lists can be used as stacks (append, pop). This code is just an illustration.

class Stack(object):
    def __init__(self, size=10):
        self._data = [None,] * size
        self._end = 0

    def push(self, value):
        self._data[self._end] = value
        self._end += 1
        if self._end >= len(self._data):
            self._grow()

    def pop(self):
        if self._end <= 0:
            return None

        value = self._data[self._end - 1]
        self._end -= 1
        return value

    def size(self):
        return self._end

    def peek(self):
        if self._end <= 0:
            return None

        return self._data[self._end - 1]

    def _grow(self):
        # DO NOT DO THIS IT IS HORRID. Just an illustration.
        new_data = [None,] * (len(self._data) * 2)
        for index in xrange(len(self._data)):
            new_data[index] = self._data[index]

        self._data = new_data


class TestStack(unittest.TestCase):
    
    def test_push_pop(self):
        stk = Stack()
        stk.push(1)
        stk.push(2)
        self.assertEqual(2, stk.pop())
        self.assertEqual(1, stk.pop())

    def test_push_pop_peek_size_grow(self):
        stk = Stack()
        quantity = 38
        for x in xrange(quantity):
            stk.push(x)
            self.assertEqual(x, stk.peek())
            self.assertEqual(x+1, stk.size())

        for x in xrange(quantity-1, -1, -1):
            self.assertEqual(x, stk.pop())

if __name__ == '__main__':
    unittest.main()

