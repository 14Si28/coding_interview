import unittest
# Ugly relative imports. These make it easy to run nosetests from the top of the repo, though. Normally, do not use relative imports.
from cracking.c01arrays import s01uniquechars
from cracking.c01arrays import s02reversestr
from cracking.c01arrays import s03removedupes
from cracking.c01arrays import s04anagram
from cracking.c01arrays import s05replacespaces
from cracking.c01arrays import s06rotatematrix
from cracking.c01arrays import s07zeromatrix
from cracking.c01arrays import s08stringrotation
from cracking.c02linkedlists import s01removedupes
from cracking.c02linkedlists import s02find
from cracking.c02linkedlists import s03deletenode
from cracking.c02linkedlists import s04adder
from cracking.c02linkedlists import s05detectcycle



class Testc01arrays(unittest.TestCase):
    def test_s01uniquechars(self):
        s01uniquechars._test_all()

    def test_s02reversestr(self):
        s02reversestr._test_all()

    def test_s03removedupes(self):
        s03removedupes._test_all()

    def test_s04anagram(self):
        s04anagram._test_all()

    def test_s05replacespaces(self):
        s05replacespaces._test_all()

    def test_s06rotatematrix(self):
        s06rotatematrix._test_all()

    def test_s07zeromatrix(self):
        s07zeromatrix._test_all()

    def test_s08stringrotation(self):
        s08stringrotation._test_all()

class Testc02linkedlists(unittest.TestCase):
    def test_s01removedupes(self):
        s01removedupes._test_all()

    def test_s02find(self):
        s02find._test_all()

    def test_s03deletenode(self):
        s03deletenode._test_all()

    def test_s04adder(self):
        s04adder._test_all()

    def test_s05detectcycle(self):
        s05detectcycle._test_all()

