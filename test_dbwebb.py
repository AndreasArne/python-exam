#!/usr/bin/env python3
# tester
import exam
import unittest
import math
from importlib import util
from unittest.mock import patch
from io import StringIO

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
        self.assertTrue(hasattr(exam, "validate_email"))
        self.assertTrue(hasattr(exam, "list_median"))
        self.assertTrue(hasattr(exam, "find_duplicates"))
    
    def test_b_validate_email(self):
        match = ["abc@gmail.com", ".@gmail.com", "ab_c@gmail.com", "ab-c@gmail.com", "aa.b-c@gmail.com", "aa.b-c@gma.il.com", "a23c@gmail.com", "abc@gmail.co3"]
        not_match = ["abcgmail.com", "@gmail.com", "abc@asf..com", "abc@.com", "ab c@gmail.com", "ab:c@gmail.com", "ab!c@gmail.com", "aåc@gmail.com", "abcgmail.c", "ab-c@gmailcom", "aa.b-c@gmail.coms", "Awac@gmail.com","aa.b-c@gmail.coms", "aa.b-c@gma@il.com"]

        for case in match:
            self.assertTrue(exam.validate_email(case))

        for case in not_match:
            self.assertFalse(exam.validate_email(case))

    def test_c_list_median(self):
        simple = [0,1,2,4,5]
        self.assertEqual(exam.list_median(simple), 2)
        unsorted = [5,1,0,2,4]
        self.assertEqual(exam.list_median(unsorted), 2)
        even = [2,1,4,5,3,2]
        self.assertEqual(exam.list_median(even), 2.5)

    def test_c_find_duplicates(self):
        empty = []
        self.assertEqual(exam.find_duplicates(empty), [])
        no_dups = ["hej", "hopp"]
        self.assertEqual(exam.find_duplicates(no_dups), [])
        dups = ["hej", "hopp", "hej"]
        self.assertEqual(exam.find_duplicates(dups), ["hej"])
        mult_dups = ["oj", "hej", "oj", "hopp", "hej"]
        self.assertEqual(exam.find_duplicates(mult_dups), ["hej", "oj"])
        upper = ["hej", "Hej"]
        self.assertEqual(exam.find_duplicates(upper), ["hej"])

    def test_d_analyze_text(self):
         self.assertIsNotNone(util.find_spec("analyze_functions"))
         inp = ["v", "p", "u", "q"]
         with patch('builtins.input', side_effect=inp):
             with patch('sys.stdout', new=StringIO()) as fake_out:
                 code = exam.analyze_text()
                 str_data = fake_out.getvalue().strip("\n")
                 list_data = str_data.split("\n")
                 self.assertEqual(list_data, ["4", "5", "6"])
                 self.assertTrue(code)


if __name__ == '__main__':
    unittest.main(verbosity=2)