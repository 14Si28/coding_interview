"""
Determine all valid end states of a game of tic tac toe. (The board state at the completion of the game.)

Alternate way of asking this: determine all possible tic tac toe board layouts.
"""

# In the rather ugly solution below, we represent the board in a list of 9 integers.
# We pre-calculate (once) the indices of all winning rows, columns, and diagonals.
# We compute every valid turn and detect wins (end states) during the recursion.
# We prevent duplicates by tracking a set with the board signature as a single string.


def _coord_to_index(x, y):
	"""
	x,y coordinates, where 0,0 is the upper left and 2,2 the lower right

	return: a list index from 0 to 8 inclusive
	"""
	return 3*y + x

def _indices_for_win():
	"""
	return: a list of lists, each sub list is a series of 3 numbers, the indices of a winning row/col/diag
	"""
	# We convert from x,y coordinates to list indices, though we could have just used list indices straightaway to avoid the conversion steps.
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
def play(board, xs_turn, next_index, all_boards, tracker):
	"""
	board: array of length 9 representing the board in order from from top left to lower right, i.e. board[0] is top left, board[3] is the first column from the left of the second row from the top, board[8] is the lower right corner.
	xs_turn: boolean True if it's player x turn
	all_boards: list of lists
	tracker: set
	"""
	board = list(board)
	board[next_index] = 'x' if xs_turn else 'o'
	if _end_game(board):
		# Prevent duplicates
		sig = ''.join(board)
		if not sig in tracker:
			tracker.add(sig)	
			all_boards.append(board)
		return
	for index in xrange(9):
		if not board[index]: # test that the cell is still open
			play(board, not xs_turn, index, all_boards, tracker)

def start_playing():
	board = ['',]*9
	all_boards = []
	play(board, True, 0, all_boards, set())
	print len(all_boards)
	for x in xrange(min(len(all_boards),100)):
		_print_board(all_boards[x])
		print

if __name__ == '__main__':
	start_playing()


