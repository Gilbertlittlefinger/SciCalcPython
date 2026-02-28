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

    def inv(self):
        c = Calculator()
        self.assertEqual(c.inv(5), .2)

    def neg(self):
        c = Calculator()
        self.assertEqual(c.neg(9), -9)

    def neg(self):
        c = Calculator()
        self.assertEqual(c.neg(-9), 9)

    def sin(self):
        c = Calculator()
        self.assertEqual(c.sin(9), 0.4121184852417566)

    def cos(self):
        c = Calculator()
        self.assertEqual(c.cos(9), -0.9111302618846769)

    def tan(self):
        c = Calculator()
        self.assertEqual(c.tan(9), 0.4523156594418099)

    def isin(self):
        c = Calculator()
        self.assertEqual(c.isin(-1), -1.5707963267948966)

    def icos(self):
        c = Calculator()
        self.assertEqual(c.icos(-1), 3.141592653589793)

    def itan(self):
        c = Calculator()
        self.assertEqual(c.itan(-1), -0.7853981633974483)

    def deg(self):
        c = Calculator()
        self.assertEqual(c.deg(45), 2578.3100780887044)
    
    def rad(self):
        c = Calculator()
        self.assertEqual(c.rad(45), 0.7853981633974483)
    
    def fac(self):
        c = Calculator()
        self.assertEqual(c.fac(9), 362880)

    def log(self):
        c = Calculator()
        self.assertEqual(c.log(9), 2.1972245773362196)

    def log10(self):
        c = Calculator()
        self.assertEqual(c.log10(9), 0.9542425094393249)

    def natlog(self):
        c = Calculator()
        self.assertEqual(c.natlog(9), 2.302585092994046)

    def in_natlog(self):
        c = Calculator()
        self.assertEqual(c.in_natlog(9), 0.43429448190325176)

    

if __name__ == '__main__':
    unittest.main()
