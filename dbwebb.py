#!/usr/bin/env python3
# tester
import exam
import unittest
import math
from importlib import util
from unittest.mock import patch

class TestFunc(unittest.TestCase):
    """
    Run the test to see when you are done improving the code.
    When you first run the test don't be discourage by
    the long execution times.
    Small improvements to the code can have big impact.
    Once b,c and d are OK uncomment e and f and run them to check.
    
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """
    

    def test_a_module(self):
        self.assertIsNotNone(util.find_spec("exam"))
    
    def test_b_area(self):
        self.assertTrue(hasattr(exam, "area"))
        self.assertEqual(exam.area(2), 4*math.pi)

    def test_c_std(self):
        inp = ["test"]
        with patch('builtins.input', side_effect=inp):
            stacks = exam.output("hahah")
        self.assertEqual(stacks, "test")

if __name__ == '__main__':
    unittest.main(verbosity=2)