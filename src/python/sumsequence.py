"""
Given an unsorted sequence of integers, find the largest sum from a subsequence.

Example:

Given: [-10, 1, 2, 5, -3]
Answer: 8 
from subsequence 1,2,5
"""

def sumsequence(numbers):
    """
    O(n)
    numbers: list of integers
    returns: largest sum of any subsequence in the list of numbers
    """
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


if __name__ == '__main__':
    i = [-10, 1, 2, 5, -3]
    print i
    m = sumsequence(i)
    print m
    assert m == 8

