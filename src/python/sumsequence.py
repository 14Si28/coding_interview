"""
Given an unsorted sequence of integers, find the largest sum from a subsequence.

Example:

Given: [-10, 1, 2, 5, -3]
Answer: 8 
from subsequence 1,2,5
"""
import unittest

def sumsequence(numbers):
    """
    O(n)
    numbers: list of integers
    returns: largest sum of any subsequence in the list of numbers
    """
    # TODO This does not work properly if all numbers are negative
    summer = list(numbers)
    min_sum = 0
    max_sum = 0
    for ind in xrange(len(summer)):
        if ind > 0: 
            summer[ind] += summer[ind - 1]

        if summer[ind] - min_sum > max_sum:
            max_sum = summer[ind] - min_sum
        if summer[ind] < min_sum:
            min_sum = summer[ind]

    return max_sum

class TestSumSequence(unittest.TestCase):
    def setUp(self):
        pass

    def test_positive_and_negative(self):
        self.assertEquals(8, sumsequence([-10, 1, 2, 5, -3]))

    def test_positive(self):
        self.assertEquals(8, sumsequence([1, 2, 5]))

    def test_zero(self):
        self.assertEquals(0, sumsequence([0]))

    def test_edge_single(self):
        self.assertEquals(8, sumsequence([8]))

    def test_edge_single_negative(self):
        self.assertEquals(-8, sumsequence([-8]))

    def test_negative(self):
        self.assertEquals(-8, sumsequence([-1, -2, -5]))


if __name__ == '__main__':
    unittest.main()


