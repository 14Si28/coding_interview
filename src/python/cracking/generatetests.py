"""
Generate unittest cases for all the Cracking problem solutions by walking dirs and python files.
We expect every solution file to have a _test_all() function.
"""
import re
import os
from os import path

# cd src/python
# python cracking/generatetests.py
# nosetests

def _append_blank_lines(output_lines, n):
    for x in xrange(n):
        output_lines.append('')

def _get_test_map(source_dir):
    solution_re = re.compile(r'^s.*\.py$') # solution files start with an 's'
    test_map = {}
    for dirpath, dirnames, filenames in os.walk(source_dir):
        package = os.path.basename(dirpath)
        test_files = sorted([os.path.splitext(x)[0] for x in filenames if solution_re.match(x)])
        test_map.setdefault(package, []).extend(test_files)
    return test_map

def _get_imports(test_pairs):
    output = ['import unittest']
    for package, test_files in test_pairs:
        for file in test_files:
            output.append('from cracking.{} import {}'.format(package, file))
    return output

def _get_test_classes(test_pairs):
    output = []
    for package, test_files in test_pairs:
        if test_files:
            output.append('class Test{}(unittest.TestCase):'.format(package))
            for file in test_files:
                output.append('    def test_{}(self):'.format(file))
                output.append('        {}._test_all()'.format(file))
                _append_blank_lines(output, 1)
    return output

def _write_output(source_dir, output_lines):
    output_lines = ['{}\n'.format(x) for x in output_lines]
    output_path = '{}/testall.py'.format(source_dir)
    with open(output_path, 'w') as output_file:
        output_file.writelines(output_lines)
    print 'Wrote test cases to: {}'.format(output_path)

def main():
    source_dir = os.path.abspath(path.dirname(__file__))
    output_lines = []
    test_pairs = sorted(_get_test_map(source_dir).iteritems())

    output_lines.extend(_get_imports(test_pairs))
    _append_blank_lines(output_lines, 3)
    output_lines.extend(_get_test_classes(test_pairs))

    _write_output(source_dir, output_lines)


if __name__ == '__main__':
    main()
