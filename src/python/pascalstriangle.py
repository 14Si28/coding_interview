"""
Generate Pascal's triangle.

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

def pascals_triangle_recursive1(height):
	def _create_triangle(height, previous_row, result):
		if height <= 0:
			return

		curr_row = [1]
		if previous_row:
			prev_col = 0
			while prev_col+1 < len(previous_row):
				elem = previous_row[prev_col] + previous_row[prev_col+1]
				curr_row.append(elem)
				prev_col += 1
			
			curr_row.append(1)

		result.append(curr_row)
		_create_triangle(height-1, curr_row, result)

	result = []
	_create_triangle(height, [], result)
	return result

def pascals_triangle_recursive2(height):
	# William Shield's solution: http://www.cforcoding.com/2012/01/interview-programming-problems-done.html
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
	_validate_func(pascals_triangle_recursive1)
	_validate_func(pascals_triangle_recursive2)
	print 'SUCCESS All tests passed.'

def main():
	# Intentionally avoiding unittest (to run via main only) and argparse (for simpler code).
	height = -1
	if len(sys.argv) > 1:
		height = int(sys.argv[1]) 

	if height < 0:
		_run_tests()
	else:
		for row in pascals_triangle_recursive1(height):
			print row

if __name__ == '__main__':
	main()

