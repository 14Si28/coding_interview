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
	_triangle(height-1, curr_row, result)

def pascals_triangle_recursive(height):
	result = []
	_triangle_recursive(height, [], result)
	return result


if __name__ == '__main__':
	height = 6
	if len(sys.argv) > 1:
		height = int(sys.argv[1]) 

	for row in pascals_triangle(height):
		print row

