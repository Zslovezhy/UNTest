# _*_ coding: utf-8 _*_
"""
Time:     2023/2/10 14:47
Author:   Sen Zhang
File:     suite_runner_login.py
Version:  V1.0  2023/2/10 14:47
Describe: 
Steps:
    1.
    2.
    ...
"""
import unittest
from testcase.test_login import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
runner = unittest.TextTestRunner()
runner.run(suite)
