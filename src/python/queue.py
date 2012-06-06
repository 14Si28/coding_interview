"""
Implement a queue using a (circular) array.
"""

# Normally in Python you would use a collections.deque if you want performant head removal (popleft). Or just use a list [] with pop(0) if performance isn't important.

import unittest

class Queue(object):
    def __init__(self, size=10):
        self._data = [None,] * size
        self._start = 0
        # Index to assign the next enqueued value.
        self._end = 0 

    def enqueue(self, value):
        if self._start == self._circular_index(self._end):
            self._grow()            

        self._data[self._end] = value
        self._end = self._circular_index(self._end)

    def dequeue(self):
        if self.is_empty():
            return None
        value = self._data[self._start]
        self._start = self._circular_index(self._start)
        return value

    def is_empty(self):
        return self._end == self._start

    def size(self):
        if self._end > self._start:
            return self._end - self._start

        return len(self._data) - self._start + self._end

    def _circular_index(self, index, direction=1):
        assert abs(direction) == 1
        index += direction
        if index >= len(self._data):
            return 0
        elif index < 0:
            return len(self._data) - 1
        return index

    def _grow(self):
        assert self._start != self._end

        # NOTE: Never write real python code like the following. This is just an illustration!
        new_data = [None,] * (len(self._data) * 2)
        
        if self._end < self._start:
            # If the queue wraps at the end, stop at the end of the array.
            end_copy = len(self._data)
        else:
            end_copy = self._end

        # Copy the start of the queue to the start of the new_data.
        new_index = 0
        for index in xrange(self._start, end_copy):
            new_data[new_index] = self._data[index]
            new_index += 1

        # If the queue wraps, copy the remaining queue elements.
        if self._start > 0 and self._end < self._start:
            for index in xrange(0, self._end):
                new_data[new_index] = self._data[index]
                new_index += 1

        self._data = new_data
        self._start = 0
        self._end = new_index
        assert new_index < len(new_data) - 1


class TestQueue(unittest.TestCase):
    def test_push_pop_one(self):
        qq = Queue()
        qq.enqueue(1)
        self.assertEquals(1, qq.dequeue())

    def test_size(self):
        qq = Queue()
        for x in xrange(100):
            qq.enqueue(x)
            self.assertEqual(x+1, qq.size())

    def test_is_empty(self):
        qq = Queue()
        self.assertTrue(qq.is_empty())
        qq.enqueue(1)
        self.assertFalse(qq.is_empty())

    def _enqueue_dequeue(self, qq, quantity):
        for x in xrange(quantity):
            qq.enqueue(x)
        for x in xrange(quantity):
            self.assertEqual(x, qq.dequeue())

    def _queue_max_size(self, qq):
        return len(qq._data)

    def test_push_pop_without_resize(self):
        qq = Queue()
        self._enqueue_dequeue(qq, self._queue_max_size(qq)-1)

    def _grow_once(self, qq):
        msize = self._queue_max_size(qq)
        self._enqueue_dequeue(qq, msize)
        self.assertNotEqual(msize, self._queue_max_size(qq))

    def test_grow(self):
        qq = Queue()
        self._grow_once(qq)
        
    def test_grow2x(self):
        qq = Queue()
        self._grow_once(qq)
        self._grow_once(qq)

    def test_circle(self):
        # Ensure that the circular array tracking is working.
        qq = Queue()
        half = self._queue_max_size(qq) / 2
        for x in xrange(half):
            qq.enqueue(x)
        # Free up some slots at the beginning of the array.
        for x in xrange(half):
            self.assertEqual(x, qq.dequeue())
        
        nearly_full = half*2 - 2 # not enough to grow
        # Add more elements to wrap around the end.
        for x in xrange(nearly_full):
            qq.enqueue(x)
        # This is the condition we're ensuring:
        self.assertTrue(qq._start > qq._end)

        for x in xrange(nearly_full):
            self.assertEqual(x, qq.dequeue())


if __name__ == '__main__':
    unittest.main()

