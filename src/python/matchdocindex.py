"""
Given a data structure that maps words to document indexes, return a list of document indexes that match all terms.
Assume that the list of document indexes are sorted in ascending order and there are no duplicates within each list.

e.g.

Given:
{ 
    'yummy': [0, 3, 7, 8],
    'japanese': [3, 5, 8],
    'ramen': [0, 1, 2, 3, 5, 8]
}

Return:
[3, 8]

This problem is a simplified presentation of word level inverted indexes. 
For more background, you can also search for:
- Word postings 
- Term frequency inverse document frequency tf*idf. 
- Book: Introduction to Information Retrieval by Manning et al
"""

def find_matches(term_postings):
    """
    term_postings: dict of lists of ints, { yummy: [0,1,2], ... }
    """
    keys = term_postings.keys()
    # The first postings seeds or matches list.
    matches = term_postings[keys[0]]
    assert sorted(matches) == matches
    # For each subsequent term...
    for key_ind in xrange(1, len(keys)):
        assert sorted(term_postings[keys[key_ind]]) == term_postings[keys[key_ind]]
        # The matched posting results are used to compare to the next postings.
        curr_postings = matches
        matches = []
        next_postings = term_postings[keys[key_ind]]

        nind = 0    
        cind = 0
        while cind < len(curr_postings) and nind < len(next_postings):
            # Find a document index in the current postings that is >= to the index in the next postings.
            while cind < len(curr_postings) and curr_postings[cind] < next_postings[nind]:
                cind += 1
            # If the doc indexes are not a match, continue looking in the next postings.
            while nind < len(next_postings) and curr_postings[cind] != next_postings[nind]:
                nind += 1
            # If the doc indexes match, move to the next index in both postings lists.
            if curr_postings[cind] == next_postings[nind]:
                matches.append(curr_postings[cind])
                cind += 1 
                nind += 1

    return matches

def _test(func, input, expected):
    actual = func(input)
    print '{}    ===>   {}'.format(input, actual)
    if actual != expected:
        raise Exception('FAIL   Expected: {}   Actual: {}'.format(expected, actual))

def _test_all():
    _test(find_matches, { 
        'yummy': [0, 3, 7, 8],
        'japanese': [3, 5, 8],
        'ramen': [0, 1, 2, 3, 5, 8]
        }, 
        [3, 8])
    _test(find_matches, { 
        'yummy': [0, 2, 3, 7, 8],
        'japanese': [2, 3, 5, 8],
        'ramen': [0, 1, 2, 3, 5, 8]
        }, 
        [2, 3, 8])
    _test(find_matches, { 
        'yummy': [0, 2, 3, 7, 8],
        'japanese': [2, 3, 5, 8],
        'spicy': [0, 1, 2, 3, 5, 6, 7, 8, 9],
        'miso': [3, 8],
        'ramen': [0, 1, 2, 3, 5, 8]
        }, 
        [3, 8])
    _test(find_matches, { 
        'yummy': [0, 1, 2, 3, 4, 5],
        'japanese': [0, 1, 2, 3, 4, 5],
        'ramen': [0, 1, 2, 3, 4, 5],
        }, 
        [0, 1, 2, 3, 4, 5])
    _test(find_matches, { 
        'yummy': [8],
        'japanese': [3, 5, 8],
        'ramen': [0, 1, 2, 3, 5, 8]
        }, 
        [8])
    _test(find_matches, { 
        'yummy': [0, 1],
        'ramen': [0, 1]
        }, 
        [0, 1])
    _test(find_matches, { 'yummy': [0, 1] },  [0, 1])
    _test(find_matches, { 'yummy': [0] }, [0])
    _test(find_matches, { 'yummy': [0] },  [0])
    _test(find_matches, { 'yummy': [] },  [])
    print 'SUCCESS'

if __name__ == '__main__':
    _test_all()