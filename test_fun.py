import unittest
from help_fun import *
# to run this test suits
# python3 -m unittest test_fun.py

class test_check(unittest.TestCase):
    def test_only_str(self):
        self.assertTrue(check("yousef"))
    
    def test_only_int(self):
        self.assertFalse(check("33"))
    
    def test_empty(self):
        self.assertFalse(check(""))

class test_check_two_symbols(unittest.TestCase):
    def test_true_contidion(self):
        self.assertTrue(check_two_symbols("x", "x", "y"))

    def test_different(self):
        self.assertFalse(check_two_symbols("d", "x", "y"))

    def test_empty(self):
        self.assertFalse(check_two_symbols("","",""))


if __name__ == "__main__":
    unittest.main()
