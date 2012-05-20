"""
Generate the README from a directory's file docstrings.
"""
import sys
import os
from os import path
import re

DOCSTR_RE = re.compile(r'^"""')
EXCLUDED_FILES = { '__init__.py' }
DOCSTR_ESCAPE_RE = re.compile(r'([\'".,:;!?\-)\]}/\>]{1})')

def main(start_path):
	print '==============================================='
	print 'Coding Interview Problem Solutions in Python'
	print '==============================================='
	print ''
	print 'Index of Files'
	print '========================'
	dirpath, dirnames, filenames = os.walk(start_path).next()
	for fn in filenames:
		print ''
		print '{}'.format(fn)
		print '________________________________'
		try:
			if not fn in EXCLUDED_FILES:
				with open(fn) as input_file:
					docstr_started = False
					summary = []
					for line in input_file:
						if re.match(DOCSTR_RE, line):
							if docstr_started:
								break
							else:
								docstr_started = True
						elif not docstr_started:
							break

						if docstr_started:
							sline = re.sub(DOCSTR_RE, '', line).strip()
							sline = re.sub(DOCSTR_ESCAPE_RE, '\\\1', sline)
							if sline:
								summary.append(line)
				print ''.join(summary)
		except Exception as ex:
			sys.stderr.write('ERROR: failed to generate summary: {}\n'.format(ex))
			print ''

if __name__ == '__main__':
	if len(sys.argv) > 1:
		start_path = sys.argv[1]
	else:
		start_path = os.getcwd()

	main(start_path)



