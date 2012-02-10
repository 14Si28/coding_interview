import unittest
# Ugly relative imports. These make it easy to run nosetests from the top of the repo, though. Normally, do not use relative imports.
from .c01arrays import s01uniquechars

class TestAllArrays(unittest.TestCase):
    def test_uniquechars(self):
        s01uniquechars._test_all()

