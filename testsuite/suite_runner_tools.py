# _*_ coding: utf-8 _*_
"""
Time:     2023/2/10 14:18
Author:   Sen Zhang
File:     suite_runner_tools.py
Version:  V1.0  2023/2/10 14:18
Describe: 
Steps:
    1.
    2.
    ...
"""
import unittest
from testcase.test_tools1 import TestAdd

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAdd))
runner = unittest.TextTestRunner()
runner.run(suite)