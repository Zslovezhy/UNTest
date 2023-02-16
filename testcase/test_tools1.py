# _*_ coding: utf-8 _*_
"""
Time:     2023/2/10 14:14
Author:   Sen Zhang
File:     test_tools1.py
Version:  V1.0  2023/2/10 14:14
Describe: 
Steps:
    1.
    2.
    ...
"""
import unittest
from tools.tools import add

class TestAdd(unittest.TestCase):

    def testAdd1(self):
        if add(1,2) == 3:
            print("正确")
        else:
            print("错误")

    def testAdd2(self):
        if add(1,2) == 10:
            print("正确")
        else:
            print("错误")

    def testAdd3(self):
        if add(3,4) == 5:
            print("正确")
        else:
            print("错误")