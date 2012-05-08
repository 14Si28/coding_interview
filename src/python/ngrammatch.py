"""
Given 2 text documents, find all 3-grams present in both documents.

An n-gram is a sequence of n items; in this problem, four words in a sequence.


Reference:
Introduction to Information Retrieval by Manning et al
Section 3.2.2 k-gram indexes for wildcard queries
Additional background (unnecessary for solving this problem): cosine similarity.
"""

import re
PUNCTUATION = re.compile(r'[.,!;]+')
WORD_SEPERATOR = re.compile(r'[\s]+')

def find_ngrams(doc1, doc2, nsize=3):
    def grammit(thedoc, nsize):
        grams = set()
        thedoc = re.sub(PUNCTUATION, '', thedoc)
        words = re.split(WORD_SEPERATOR, thedoc)
        for ind in xrange(len(words)):
            g = ' '.join(words[ind:ind+nsize])
            grams.add(g)
        return grams

    doc1_grams = grammit(doc1, nsize)
    doc2_grams = grammit(doc2, nsize)
    # set intersection complexity:  average: O(min(len(s), len(t)) ,  worst: O(len(s) * len(t))   # http://wiki.python.org/moin/TimeComplexity
    return list(doc1_grams.intersection(doc2_grams))

def _test(doc1, doc2, expected):
    actual = find_ngrams(doc1, doc2)
    if sorted(actual) != sorted(expected):
        raise Exception('FAIL (Ignored order) Expected: {}   Actual: {}'.format(expected, actual))
    print '___________'
    print 'doc1: {}'.format(doc1)
    print 'doc2: {}'.format(doc2)
    print '=====> {}'.format(actual)

def _test_all():
    _test('The quick brown fox jumps over the lazy dog. The rain in Spain falls mostly on the plains.',
        'The rain in Spain makes the lazy dog very sad, while the brown fox jumps over the moon with a cow.',
        ['brown fox jumps', 'the lazy dog', 'rain in Spain', 'jumps over the', 'The rain in', 'fox jumps over'])

if __name__ == '__main__':
    _test_all()

