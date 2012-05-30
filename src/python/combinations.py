"""
Generate all combinations of a list of choices.
"""

def all_combinations(values):
	if not values:
		return []
	results = []
	for index, c in enumerate(values):
		results.append([c])
		if index < len(values)-1:
			next_combos = all_combinations(values[index+1:])
			for x in next_combos:
				t = [c]
				t.extend(x)
				results.append(t)

	return results

def _test_one(func, input, expected):
	actual = func(input)
	actual = sorted(actual)
	expected = sorted(expected)
	print '__________ {}'.format(func)
	print '{}  ===> {}'.format(input, actual)
	if actual != expected:
		raise Exception('FAIL Expected: {}  Actual: {}'.format(expected, actual))

def _test_all(func):
	_test_one(func, [1,2,3], [[1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
	_test_one(func, list('wxyz'), [['w'], ['w', 'x'], ['w', 'x', 'y'], ['w', 'x', 'y', 'z'], ['w', 'x', 'z'], ['w', 'y'], ['w', 'y', 'z'], ['w', 'z'], ['x'], ['x', 'y'], ['x', 'y', 'z'], ['x', 'z'], ['y'], ['y', 'z'], ['z']])

if __name__ == '__main__':
	_test_all(all_combinations)