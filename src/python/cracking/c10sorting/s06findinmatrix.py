"""
Given an M x N matrix in which each row and column is sorted in ascending order, write a method to find an element.
"""

def find_in(matrix, to_find):
	"""
	PRE: matrix is a list of lists, outer list is rows, inner lists are column values, values are sorted ascending across rows and columns.
	"""
	row = 0
	col = len(matrix[0]) - 1
	while row < len(matrix) and col >= 0:
		if matrix[row][col] == to_find:
			return row, col
		elif matrix[row][col] > to_find:
			col -= 1
		else: # cell < to_find
			row += 1

	return None

def _test_one(matrix, to_find, expected):
	actual = find_in(matrix, to_find)
	if actual != expected:
		raise Exception('FAIL Expected: {} Actual: {}'.format(expected, actual))

def _test_all():
	matrix1 = [[15, 20, 40, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]]
	_test_one(matrix1, 55, (2, 1)) # row 2, column 1

if __name__ == '__main__':
	_test_all()

