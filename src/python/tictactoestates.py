"""
Determine all valid end states of a game of tic tac toe. (The board state at the completion of the game.)

Alternate way of asking this: determine all possible tic tac toe board layouts.
"""


def _coord_to_index(x, y):
	return 3*y + x

def _indices_for_win():
	indices = []
	# columns
	for x in xrange(3):
		line = []
		for y in xrange(3):
			line.append(_coord_to_index(x, y))
		indices.append(line)

	# rows
	for y in xrange(3):
		line = []
		for x in xrange(3):
			line.append(_coord_to_index(x, y))
		indices.append(line)

	# diagonals 
	line = []
	for x, y in [ (0,0), (1,1), (2,2) ]:
		line.append(_coord_to_index(x, y))
	indices.append(line)

	line = []
	for x, y in [ (2,0), (1,1), (0,2) ]:
		line.append(_coord_to_index(x, y))
	indices.append(line)

	return indices

def _print_board(board):
	for y in xrange(3):
		for x in xrange(3):
			cell = board[_coord_to_index(x, y)]
			if not cell:
				cell = '_'
			print cell,
		print

WINNING_INDICES = _indices_for_win()

def _end_game(board):
	for line in WINNING_INDICES:
		first = board[line[0]]
		if first:
			won = True
			for x in line[1:]:
				if board[x] != first:
					won = False
			if won:
				return True

	return False

# Rough overestimate of possible turns (not end states): 9!
def play(board, xs_turn, next_index, all_boards):
	"""
	board: array of length 9 representing the board in order from from top left to lower right, i.e. board[0] is top left, board[3] is the first column from the left of the second row from the top, board[8] is the lower right corner.
	"""
	board = list(board)
	board[next_index] = 'x' if xs_turn else 'o'
	if _end_game(board):
		all_boards.append(board)
		return
	for index in xrange(9):
		if not board[index]:
			play(board, not xs_turn, index, all_boards)

def start_playing():
	board = [None,]*9
	all_boards = []
	play(board, True, 0, all_boards)
	print len(all_boards)
	for x in xrange(100):
		_print_board(all_boards[x])
		print

if __name__ == '__main__':
	start_playing()


