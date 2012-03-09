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

def _triangle_recursive(height, previous_row, result):
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
	_triangle_recursive(height-1, curr_row, result)

def pascals_triangle_recursive(height):
	result = []
	_triangle_recursive(height, [], result)
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

def _hard_coded_validation(func):
	actual_triangle = func(len(EXPECTED_VALUES))
	for expected, actual in itertools.izip(EXPECTED_VALUES, actual_triangle):
		assert expected == actual
	assert len(EXPECTED_VALUES) == len(actual_triangle)

def _run_tests():
	_hard_coded_validation(pascals_triangle_recursive)
	print 'SUCCESS All tests passed.'

def main():
	# Intentionally avoiding unittest (to run via main only) and argparse (for simpler code).
	height = -1
	if len(sys.argv) > 1:
		height = int(sys.argv[1]) 

	if height < 0:
		_run_tests()
	else:
		for row in pascals_triangle_recursive(height):
			print row

if __name__ == '__main__':
	main()

