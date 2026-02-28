import math
import unittest
from calculator import Calculator


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(3, 3), 6)

    def test_add2(self):
        c = Calculator()
        self.assertEqual(c.add(12, -10), 2)

    def test_add3(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_sub(self):
        c = Calculator()
        self.assertEqual(c.sub(9, 3), 6)

    def test_mult(self):
        c = Calculator()
        self.assertEqual(c.mult(9, 3), 27)

    def test_div(self):
        c = Calculator()
        self.assertEqual(c.div(9, 3), 3)

    def test_div(self):
        c = Calculator()
        self.assertEqual(c.sqr(9), 81)

    def test_root2(self):
        c = Calculator()
        self.assertEqual(c.root2(9), 3)

    def test_exp(self):
        c = Calculator()
        self.assertEqual(c.exp(9,3), 729)

if __name__ == '__main__':
    unittest.main()
