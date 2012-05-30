"""
Generate all permutations of balanced parenthesis given a quantity of pairs.

* n = 1: ['()']
* n = 2: ['()()', '(())']
* n = 3: ['()(())', '((()))', '(()())', '(())()', '()()()']
"""

def gen_parens(n):
    """
    O(n!) ?
    """
    if n <= 1:
        return [ '()' ]
    
    prev = gen_parens(n-1)
    result = set()
    for a in prev:
        for index in xrange(len(a)):
            curr = list(a)
            curr.insert(index, '()')
            result.add(''.join(curr))
    
    return result

def gen_parens_strs(n):
    lol = gen_parens(n)
    results = []
    for a in lol:
        results.append(''.join(a))
    return results

if __name__ == '__main__':
    for x in xrange(1, 5): 
        print gen_parens_strs(x)
