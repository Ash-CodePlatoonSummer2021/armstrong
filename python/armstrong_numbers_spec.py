# The code is written as driver code. Can you convert it to Unit Test?
from armstrong_numbers import find_armstrong_numbers
import unittest

class armstrongTestCase(unittest.TestCase):

    """Tests for `armstrong_numbers.py`"""

    def testZero(self):
        self.assertEqual(find_armstrong_numbers([0]),[0])
    def test8(self):
        self.assertEqual(find_armstrong_numbers(list(range(0, 8))),[0, 1, 2, 3, 4, 5, 6, 7])
    def test100(self):
        self.assertEqual(find_armstrong_numbers(list(range(0, 100))),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    def test1000(self):
        self.assertEqual(find_armstrong_numbers(list(range(0, 999))),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])


t =  armstrongTestCase()
t.testZero()
t.test8()
t.test100()
t.test1000()
