"""
Generate unittest cases for all the cracking solutions by walking dirs and python files.
"""
import re
import os
from os import path

# python src/python/cracking/generatetests.py

def _append_blank_lines(output_lines, n):
    for x in xrange(n):
        output_lines.append('')

def main():
    source_dir = os.path.abspath(path.dirname(__file__))
    output_lines = []
    solution_re = re.compile(r'^s.*\.py$')
    test_map = {}
    for dirpath, dirnames, filenames in os.walk(source_dir):
        package = os.path.basename(dirpath)
        test_files = sorted([os.path.splitext(x)[0] for x in filenames if solution_re.match(x)])
        if test_files:
            test_map.setdefault(package, []).extend(test_files)


    output_lines.append('import unittest')
    output_lines.append('# Ugly relative imports. These make it easy to run nosetests from the top of the repo, though. Normally, do not use relative imports.')

    test_pairs = sorted(test_map.iteritems())
    for package, test_files in test_pairs:
        for file in test_files:
            output_lines.append('from cracking.{} import {}'.format(package, file))

    _append_blank_lines(output_lines, 3)

    for package, test_files in test_pairs:
        output_lines.append('class Test{}(unittest.TestCase):'.format(package))
        for file in test_files:
            output_lines.append('    def test_{}(self):'.format(file))
            output_lines.append('        {}._test_all()'.format(file))
            _append_blank_lines(output_lines, 1)

    output_lines = ['{}\n'.format(x) for x in output_lines]
    output_path = '{}/testall.py'.format(source_dir)
    with open(output_path, 'w') as output_file:
        output_file.writelines(output_lines)
    print 'Wrote test cases to: {}'.format(output_path)


if __name__ == '__main__':
    main()
