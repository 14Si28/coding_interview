"""
Generate Pascal's triangle::

            1
          1, 1
         1, 2, 1
        1, 3, 3, 1
      1, 4, 6, 4, 1
    1, 5, 10, 10, 5, 1

"""
import sys
import itertools
import math

def pascals_triangle1(height):
    """
    Recursive impl. This one's naive and not pythonic (note the use of len, index, and a result accumulator param). It's also a bad mix of iterative and recursive.

    returns: a pascal's triangle as a list of lists.
    """
    def _create_triangle(height, previous_row, result):
        if height <= 0:
            return

        # Rows always start with 1
        curr_row = [1]
        if previous_row: # previous_row is empty for the first computed row 
            prev_col = 0
            while prev_col+1 < len(previous_row):
                # The next element is the sum of the 2 adjacent elements in the  previous row.
                elem = previous_row[prev_col] + previous_row[prev_col+1]
                curr_row.append(elem)
                prev_col += 1
            
            curr_row.append(1)

        result.append(curr_row)
        _create_triangle(height-1, curr_row, result)

    result = []
    _create_triangle(height, [], result)
    return result

def pascals_triangle2(height):
    """
    Recursive impl. See William Shield's post: http://www.cforcoding.com/2012/01/interview-programming-problems-done.html
    This one's inefficient.

    returns: a pascal's triangle as a list of lists.
    """
    def _elem(row_index, col_index):
        if col_index < 0 or col_index > row_index:
            return 0
        if col_index == 0 or col_index == row_index:
            return 1
        return _elem(row_index-1, col_index-1) + _elem(row_index-1, col_index)
 
    def _row(row_index):
        return [_elem(row_index, x) for x in xrange(row_index+1)]
 
    result = []
    for i in xrange(height):
        result.append(_row(i))
    return result

def pascals_triangle3(height):
    """
    Iterative impl. Compact and pythonic.

    returns: a pascal's triangle as a list of lists.
    """
    if height < 1:
        return []
    rows = [[1]]
    for row_num in xrange(1, height):
        cells = [1]
        prev_row = rows[-1]
        for col_num in xrange(0, len(prev_row)-1):
            cells.append(prev_row[col_num] + prev_row[col_num+1])
        
        cells.append(1)
        rows.append(cells)

    return rows

def pascals_triangle4(height):
    """
    Another iterative impl, by teejae.
    """
    def _row(prev_row):
        r = [1]
        if not prev_row:
            return r
        for i in xrange(len(prev_row)-1):
            r.append(prev_row[i] + prev_row[i+1])

        r.append(1)

        return r

    t = []
    pr = None
    for i in xrange(height):
        pr = _row(prev_row=pr)
        t.append(pr)

    return t



############################################
# Tests 
#

EXPECTED_VALUES = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
]

MAX_HEIGHT = 16

def _hard_coded_validation(func):
    actual_triangle = func(len(EXPECTED_VALUES))
    for expected, actual in itertools.izip(EXPECTED_VALUES, actual_triangle):
        assert expected == actual
    assert len(EXPECTED_VALUES) == len(actual_triangle)

def _pascals_element(row, col):
    """
    row: 0 based index of the pascal's triangle row
    col: 0 based index of the element within a row

    returns: the value of the specifed element in the row
    """
    # n! / ( r! * (n - r)! )    where n is row, r is element w/in the row
    return math.factorial(row) / ( math.factorial(col) * math.factorial(row - col) )

def _validate_row(row_index, row_values):
    assert row_index + 1 == len(row_values)

    for col in xrange(len(row_values)):
        expected = _pascals_element(row_index, col)
        assert expected == row_values[col]

def _validate_triangle(height, triangle_rows):
    assert height == len(triangle_rows)
    print triangle_rows
    for index in xrange(len(triangle_rows)):
        _validate_row(index, triangle_rows[index])

def _validate_func(func):
    _hard_coded_validation(func)

    for height in xrange(1, MAX_HEIGHT+1):
        _validate_triangle(height, func(height))

def _run_tests():
    _validate_func(pascals_triangle1)
    _validate_func(pascals_triangle2)
    _validate_func(pascals_triangle3)
    _validate_func(pascals_triangle4)
    print 'SUCCESS All tests passed.'

def main():
    # Intentionally avoiding unittest (to run via main only) and argparse (for simpler code).
    height = -1
    if len(sys.argv) > 1:
        height = int(sys.argv[1]) 

    if height < 0:
        _run_tests()
    else:
        for row in pascals_triangle1(height):
            print row

if __name__ == '__main__':
    main()

