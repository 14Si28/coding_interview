"""
Generate the README from a directory's file docstrings.
"""
import sys
import os
from os import path
import re

DOCSTR_RE = re.compile(r'^"""')
EXCLUDED_FILES = { '__init__.py', 'README.rst', 'tmp.html', 'README.html' }

HEADER = """===============================================
Coding Interview Problem Solutions in Python
===============================================

Cracking the Coding Interview
=================================

See `the cracking subdir <./cracking>`_.

Index of Files in This Directory
===================================
"""

def _print_section(filename):
	print ''
	#print '{}'.format(filename)
	# The ./python subdir is off the git base of tree/master/src
	print '`{} <./python/{}>`_'.format(filename, filename)
	print '____________________________________________________________________'

def _summary(input_file):
	docstr_started = False
	summary = []
	for line in input_file:
		if re.match(DOCSTR_RE, line):
			line = re.sub(DOCSTR_RE, '', line)
			if docstr_started:
				break
			else:
				docstr_started = True
		elif not docstr_started:
			break

		if docstr_started:
			summary.append(line)
	return ''.join(summary)

def main(start_path):
	print HEADER
	dirpath, dirnames, filenames = os.walk(start_path).next()
	for fn in filenames:
		if fn in EXCLUDED_FILES:
			continue
		_print_section(fn)
		try:
			with open(fn) as input_file:
				print _summary(input_file)
		except Exception as ex:
			sys.stderr.write('ERROR: failed to generate summary: {}\n'.format(ex))
			print ''

if __name__ == '__main__':
	if len(sys.argv) > 1:
		start_path = sys.argv[1]
	else:
		start_path = os.getcwd()

	main(start_path)



