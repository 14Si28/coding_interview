===============================================
Coding Interview Problem Solutions in Python
===============================================

Cracking the Coding Interview
=================================

See `the cracking subdir <./python/cracking>`_.

Index of Files in This Directory
===================================


`combinations.py <./python/combinations.py>`_
____________________________________________________________________

Generate all combinations of a list of choices.


`factorial.py <./python/factorial.py>`_
____________________________________________________________________

Write an algorithm to compute n factorial (n!).


`factorialzeros.py <./python/factorialzeros.py>`_
____________________________________________________________________

Write an algorithm that calculates the total number of zeros in n factorial (n!).

Variant: count only the trailing zeros.


`fibonacci.py <./python/fibonacci.py>`_
____________________________________________________________________

Generate Fibonacci numbers with two different implementations.
"the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two."

n: 0,1,2,3,4,5,6, 7, 8, 9,10,11, 12
f: 0,1,1,2,3,5,8,13,21,34,55,89,144


`fifoqueue.py <./python/fifoqueue.py>`_
____________________________________________________________________

Create a simple FIFO queue, and separately a fixed size FIFO queue, each with add(), remove(), and count() *methods* (no properties).

Clearly unnecessary in Python.


`fizzbuzz.py <./python/fizzbuzz.py>`_
____________________________________________________________________

Fizz buzz aka bizz buzz. 

Count from 0 to 100, replacing any number divisible by 3 with fizz, divisible by 5 with buzz, 
and divisible by both 3 and 5 with fizz buzz.


`gameoflife.py <./python/gameoflife.py>`_
____________________________________________________________________

Conway's Game of Life
Any live cell with fewer than two live neighbours dies, as if caused by under-population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


`genreadme.py <./python/genreadme.py>`_
____________________________________________________________________

Generate the README from a directory's file docstrings.


`insertionsort.py <./python/insertionsort.py>`_
____________________________________________________________________

Insertion sort.

O(n) best, O(n^2) worst.


`linkedlistfindnth.py <./python/linkedlistfindnth.py>`_
____________________________________________________________________

Find the nth value from the end of a singly linked list.


`matchdocindex.py <./python/matchdocindex.py>`_
____________________________________________________________________

Given a data structure that maps words to document indexes, return a list of document indexes that match all terms.
Assume that the list of document indexes are sorted in ascending order and there are no duplicates within each list.

e.g.

Given::

    { 
        'yummy': [0, 3, 7, 8],
        'japanese': [3, 5, 8],
        'ramen': [0, 1, 2, 3, 5, 8]
    }

Return::

    [3, 8]

This problem is a simplified presentation of word level inverted indexes. 
You don't need to know inverted indexes or how to merge posting lists to solve this problem.
For more background, you can also search for:
* Word postings and posting lists
* Term frequency inverse document frequency tf*idf. 
* Book: Introduction to Information Retrieval by Manning et al


`mergesort.py <./python/mergesort.py>`_
____________________________________________________________________

Merge sort.

O(n log n), stable.


`multiplyarray.py <./python/multiplyarray.py>`_
____________________________________________________________________

Given an array of integers, return a new array where each element is 
the product of all other elements from the original array except that index.

e.g.
Given [3, 8, 2]
Return [16, 6, 24]
Which is [(8*2), (3*2), (3*8)]

Follow up questions: Can you make it O(n)? How would you test it for correctness? What about negative numbers and 0's?


`mvc.py <./python/mvc.py>`_
____________________________________________________________________

Simplified MVC examples.


`mvvm.py <./python/mvvm.py>`_
____________________________________________________________________

Simplified MVVM ( Model View ViewModel ) example.
MVVM is a pattern commonly used in .NET WPF, a specialization of MVP, PM, and its variants.
This pattern is almost never used in Python; this is an illustration.


`ngrammatch.py <./python/ngrammatch.py>`_
____________________________________________________________________

Given 2 text documents, find all 3-grams present in both documents.

An n-gram is a sequence of n items; in this problem, three words in a sequence.


Reference:
Introduction to Information Retrieval by Manning et al
Section 3.2.2 k-gram indexes for wildcard queries
Additional background (unnecessary for solving this problem): cosine similarity.


`nthsmallest.py <./python/nthsmallest.py>`_
____________________________________________________________________

Find the nth smallest integer in an array of integers.

Follow up question: make this work effeciently with billions of integers.


`pascalstriangle.py <./python/pascalstriangle.py>`_
____________________________________________________________________

Generate Pascal's triangle::

            1
          1, 1
         1, 2, 1
        1, 3, 3, 1
      1, 4, 6, 4, 1
    1, 5, 10, 10, 5, 1



`permutations.py <./python/permutations.py>`_
____________________________________________________________________

Generate all permutations of characters in a given input string, e.g. 'ab' ==> { 'ab', 'ba' }


`permuteparens.py <./python/permuteparens.py>`_
____________________________________________________________________

Generate all permutations of balanced parenthesis given a quantity of pairs.

* n = 1: ['()']
* n = 2: ['()()', '(())']
* n = 3: ['()(())', '((()))', '(()())', '(())()', '()()()']


`permutermspell.py <./python/permutermspell.py>`_
____________________________________________________________________

Given a dictionary of words (English and other languages), then given an input search term, 
determine all valid words that differ by only one character 
(anywhere in the input term). No additional characters are added, 
i.e. the length of the search term matches the length of the alternate words.

"lair"  ==> fair, airy,  ...
"ball" ==> fall, wall, tall, bail, Bali ...

Follow up: what if the dictionary has hundreds of millions of words?
Variation: what if you must generate the variations? 


`prefixnotation.py <./python/prefixnotation.py>`_
____________________________________________________________________

Implement a calculator for prefix notation (Polish notation).

Examples::

    + 3 5
    performs: 3 + 5
    result: 8

    * + 1 1 4
    performs: (1 + 1) * 4
    result: 8

    / * 1 + 2 6 4
    performs: (1 * ( 2 + 6 )) / 4
    result: 2



`quicksort.py <./python/quicksort.py>`_
____________________________________________________________________

Quicksort illustration. 

There are many quicksort variations and tweaks; this file just covers some basics.

Note: in Python use sorted() instead (Timsort).


`rangemap.py <./python/rangemap.py>`_
____________________________________________________________________

Given an integer, return a string. There is an integer range that always returns a particular string for that range.

e.g.

* 1,2,3...9 => "kitten"
* 10,11,12..19 => "chicklet"
* 20,21,22..49 => "calf"
* 10000..393451 => "bunny"
* 393452..598274 => "puppy"

There is no pattern to the beginning or ending of each range, but the numbers within a range are guaranteed to be contiguous. 
The ranges are known up front, but assume there could be many millions of ranges.


`secretsanta.py <./python/secretsanta.py>`_
____________________________________________________________________

Secret Santa problem: exchange of presents among a group. 
Given a list of names, each person gives one present to one other person. 
Everyone must give only one present, and each must receive one present. 
The exchange cannot be reciprocal, e.g. if person A gives to B, B cannot give to A. 

Create an algorithm that, as randomly as possible, assigns givers and recipients.

Then prove that it works correctly.


`shuffling.py <./python/shuffling.py>`_
____________________________________________________________________

Implement a fair randomized shuffling algorithm for a deck of cards.


`skiplist.py <./python/skiplist.py>`_
____________________________________________________________________

Illustrate a skip list search.


`sortrgb.py <./python/sortrgb.py>`_
____________________________________________________________________

Sorting exercise as an interview question, as seen in the wild. 

This is a variant of the Dutch national flag problem (Dijkstra).


Suppose that we have three object types R, G, and B, and an array containing objects of
those types:

{ g, r, b, r, r, g, g }

The goal is to write a function that will, in place, rearrange the elements such
that all R's appear at the beginning of the array, G's in the middle and B's at
the end. For the input above, by the end of execution the input array should look like:

{ r, r, r, g, g, g, b }

The goal is to solve this as efficiently as possible, optimizing O() runtime,
O() space. The ideal solution uses O(1) space and only makes one pass through the array.

Assume you have global functions::

    bool isR(Object *o);
    bool isG(Object *o);
    bool isB(Object *o);

to test each object type.

Please do not use external resources like compilers and Google. We expect you to verify
the code yourself without other help.


`sumsequence.py <./python/sumsequence.py>`_
____________________________________________________________________

Given an unsorted sequence of integers, find the largest sum from a subsequence.

Example:

Given: [-10, 1, 2, 5, -3]
Answer: 8 
from subsequence 1,2,5


`tictactoestates.py <./python/tictactoestates.py>`_
____________________________________________________________________

Determine all valid end states of a game of tic tac toe. (The board state at the completion of the game.)

Alternate way of asking this: determine all possible tic tac toe board layouts.


`timeremain.py <./python/timeremain.py>`_
____________________________________________________________________

Convert a remaining time in seconds to its components (remaining hours, minutes, seconds).


`treeancestor.py <./python/treeancestor.py>`_
____________________________________________________________________

Given a binary search tree with integer values sorted from lowest to highest (left nodes lower than right nodes), with no duplicates,
find the lowest level common ancestor of two target values.


`treebalance.py <./python/treebalance.py>`_
____________________________________________________________________

Convert a sorted array to a balanced binary search tree (BST).
The array is sorted in ascending order.


`treebfs.py <./python/treebfs.py>`_
____________________________________________________________________

Illustrate a breadth first search in a binary tree.


`treebinarysearch.py <./python/treebinarysearch.py>`_
____________________________________________________________________

Illustrate binary search.


`treeserialize.py <./python/treeserialize.py>`_
____________________________________________________________________

Create functions to serialize a binary tree to a string and deserialize it from a string.

