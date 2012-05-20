===============================================
Coding Interview Problem Solutions in Python
===============================================

Cracking the Coding Interview
=================================

See `the cracking subdir <./cracking>`_.

Index of Files in This Directory
===================================


`fibonacci.py <./fibonacci.py>`_
____________________________________________________________________

Generate Fibonacci numbers with two different implementations.
"the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two."
0,1,1,2,3,5,8,13,21,34,55,89,144


`fifoqueue.py <./fifoqueue.py>`_
____________________________________________________________________

Create a simple FIFO queue, and separately a fixed size FIFO queue, each with add(), remove(), and count() *methods* (no properties).

Clearly unnecessary in Python.


`fizzbuzz.py <./fizzbuzz.py>`_
____________________________________________________________________

Fizz buzz aka bizz buzz. 

Count from 0 to 100, replacing any number divisible by 3 with fizz, divisible by 5 with buzz, 
and divisible by both 3 and 5 with fizz buzz.


`gameoflife.py <./gameoflife.py>`_
____________________________________________________________________

Conway's Game of Life
Any live cell with fewer than two live neighbours dies, as if caused by under-population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


`genreadme.py <./genreadme.py>`_
____________________________________________________________________

Generate the README from a directory's file docstrings.


`matchdocindex.py <./matchdocindex.py>`_
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
You don't need to know inverted indexes or document classification to solve this problem.
For more background, you can also search for:
* Word postings and posting lists
* Term frequency inverse document frequency tf*idf. 
* Book: Introduction to Information Retrieval by Manning et al


`mvc.py <./mvc.py>`_
____________________________________________________________________

Simplified MVC examples.


`mvvm.py <./mvvm.py>`_
____________________________________________________________________

Simplified MVVM ( Model View ViewModel ) example.
MVVM is a pattern commonly used in .NET WPF, a specialization of MVP, PM, and its variants.
This pattern is almost never used in Python; this is an illustration.


`ngrammatch.py <./ngrammatch.py>`_
____________________________________________________________________

Given 2 text documents, find all 3-grams present in both documents.

An n-gram is a sequence of n items; in this problem, three words in a sequence.


Reference:
Introduction to Information Retrieval by Manning et al
Section 3.2.2 k-gram indexes for wildcard queries
Additional background (unnecessary for solving this problem): cosine similarity.


`nthsmallest.py <./nthsmallest.py>`_
____________________________________________________________________

Find the nth smallest integer in an array of integers.

Follow up question: make this work effeciently with billions of integers.


`pascalstriangle.py <./pascalstriangle.py>`_
____________________________________________________________________

Generate Pascal's triangle::

            1
          1, 1
         1, 2, 1
        1, 3, 3, 1
      1, 4, 6, 4, 1
    1, 5, 10, 10, 5, 1



`permutationcombo.py <./permutationcombo.py>`_
____________________________________________________________________

Generate all permutations of characters in a given input string, e.g. 'ab' ==> { 'ab', 'ba' }


`prefixnotation.py <./prefixnotation.py>`_
____________________________________________________________________

Implement a calculator for prefix notation (Polish notation).

Examples:
+ 3 5
performs: 3 + 5
result: 8

\* + 1 1 4
performs: (1 + 1) * 4
result: 8

/ \* 1 + 2 6 4
performs: (1 * ( 2 + 6 )) / 4
result: 2


`quicksort.py <./quicksort.py>`_
____________________________________________________________________

Quicksort illustration. 

There are many quicksort variations and tweaks; this file just covers some basics.

Note: in Python use sorted() instead (Timsort).


`README.rst <./README.rst>`_
____________________________________________________________________


`secretsanta.py <./secretsanta.py>`_
____________________________________________________________________

Secret Santa problem: exchange of presents among a group. 
Given a list of names, each person gives one present to one other person. 
Everyone must give only one present, and each must receive one present. 
The exchange cannot be reciprocal, e.g. if person A gives to B, B cannot give to A. 

Create an algorithm that, as randomly as possible, assigns givers and recipients.

Then prove that it works correctly.


`sortrgb.py <./sortrgb.py>`_
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


`sumsequence.py <./sumsequence.py>`_
____________________________________________________________________

Given an unsorted sequence of integers, find the largest sum from a subsequence.

Example:

Given: [-10, 1, 2, 5, -3]
Answer: 8 
from subsequence 1,2,5


`termspellcombo.py <./termspellcombo.py>`_
____________________________________________________________________

Given a dictionary of words (English and other languages), then given an input search term, 
determine all valid words that differ by only one character 
(anywhere in the input term). No additional characters are added, 
i.e. the length of the search term matches the length of the alternate words.

"lair"  ==> fair, airy,  ...
"ball" ==> fall, wall, tall, bail, Bali ...

Follow up: what if the dictionary has hundreds of millions of words?
Variation: what if you must generate the variations? 


`tictactoestates.py <./tictactoestates.py>`_
____________________________________________________________________

Determine all valid end states of a game of tic tac toe. (The board state at the completion of the game.)

Alternate way of asking this: determine all possible tic tac toe board layouts.


`timeremain.py <./timeremain.py>`_
____________________________________________________________________

Convert a remaining time in seconds to its components (remaining hours, minutes, seconds).


`tmp.html <./tmp.html>`_
____________________________________________________________________


`treebfs.py <./treebfs.py>`_
____________________________________________________________________

Illustrate a breadth first search in a binary tree.

