"""
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
"""

import re

VALID_RE = re.compile(r'^[-+*/]\s+(([-+*/]|-?[0-9]+)(\s+|$))+$')
SEPARATOR_RE = re.compile(r'([-+*/]|-?[0-9]+)(\s+|$)')
OPERATOR_RE = re.compile(r'[-+*/]')
NUMBER_RE = re.compile(r'-?[0-9]')

def calculator(input):
    if not VALID_RE.match(input):
        raise Exception('Invalid input: {}'.format(input))

    # Use regex to tokenize the string, removing any whitespace elements.
    items = [x for x in SEPARATOR_RE.split(input) if x and x.strip()]
    if not items:
        raise Exception('Invalid input (insufficient operators or operands): {}'.format(input))
    

    def apply(operator, left, right):
        print '({} {} {})'.format(left, operator, right)
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        raise Exception('Invalid operator: {}'.format(operator))

    # LIFO
    stack = []
    # Process items back to front.
    list.reverse(items)
    try:
        for item in items:
            if NUMBER_RE.match(item):
                stack.append(int(item))
            elif OPERATOR_RE.match(item):
                stack.append(apply(item, stack.pop(), stack.pop()))
            else:
                raise Exception('Invalid item: {}'.format(item))

        assert len(stack) == 1
        return stack.pop()

    except Exception as ex:
        print 'ERROR: {}   Stack: {}'.format(ex, stack)
        raise

def _test(input, expected):
    actual = calculator(input)
    if actual != expected:
        raise Exception('FAIL Expected: {}  Actual: {}'.format(expected, actual))
    print '{}    ===> {}'.format(input, actual)

def _test_all():
    _test('/ * 1 + 2 6 4', 2)
    _test('- * / 15 - 7 + 1 1 3 + 2 + 1 1', 5)
    _test('/ * -1 + -2 -6 -4', -2)
    _test('* + 1 1 4', 8)
    print 'SUCCESS'

if __name__ == '__main__':
    _test_all()




