import unittest
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
from cracking.c03stacks import s04towersofhanoi
from cracking.c04trees import s01treebalanced
from cracking.c04trees import s08subtree
from cracking.c07maths import s04division
from cracking.c09recursion import s01stairs
from cracking.c10sorting import s06findinmatrix



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

class Testc03stacks(unittest.TestCase):
    def test_s04towersofhanoi(self):
        s04towersofhanoi._test_all()

class Testc04trees(unittest.TestCase):
    def test_s01treebalanced(self):
        s01treebalanced._test_all()

    def test_s08subtree(self):
        s08subtree._test_all()

class Testc07maths(unittest.TestCase):
    def test_s04division(self):
        s04division._test_all()

class Testc09recursion(unittest.TestCase):
    def test_s01stairs(self):
        s01stairs._test_all()

class Testc10sorting(unittest.TestCase):
    def test_s06findinmatrix(self):
        s06findinmatrix._test_all()

