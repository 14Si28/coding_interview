"""
Simple FIFO queue and a fixed size FIFO queue with add(), remove(), and count() *methods* (no properties).
Clearly unnecessary in Python.
"""

class FifoQueue(object):
    def __init__(self):
        self._queue = []

    def add(self, x):
        self._queue.append(x)

    def remove(self):
        if self.count() <= 0:
            raise Exception('Queue is empty.')
        return self._queue.pop(0)

    def count(self):
        return len(self._queue)

class FifoQueueFixedSize(object):
    def __init__(self, max_size=10):
        self._queue = []
        self._max_size = max_size

    def add(self, x):
        if self.count()  >= self._max_size:
            raise Exception('Queue is full.')
        self._queue.append(x)

    def remove(self):
        if self.count() <= 0:
            raise Exception('Queue is empty.')
        return self._queue.pop(0)

    def count(self):
        return len(self._queue)


    
#################################################
# Tests

def _test_remove_when_empty(q):
    fail = False
    try:
        q.remove()
        fail = True
    except Exception:
        pass
    if fail:
        raise Exception('Remove must throw an exception when queue empty.')

def _test_fifo_queue():
    q = FifoQueue()
    q.add(0)
    q.add(1)
    q.add(2)
    assert q.remove() == 0
    assert q.remove() == 1
    assert q.remove() == 2
    _test_remove_when_empty(q)

def _test_fifo_queue_fixed_size():
    q = FifoQueueFixedSize()
    quantity = 10
    for x in xrange(quantity):
        q.add(x)

    fail = False
    try:
        q.add(11)
        fail = True
    except Exception:
        pass
    if fail:
        raise Exception('Add must throw an exception when queue full.')

    for x in xrange(quantity):
        assert q.remove() == x

    _test_remove_when_empty(q)


if __name__ == '__main__':
    print 'Testing FifoQueue...'
    _test_fifo_queue()
    _test_fifo_queue_fixed_size()
    print 'SUCCESS'







