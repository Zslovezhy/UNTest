# _*_ coding: utf-8 _*_
"""
Time:     2023/2/15 15:04
Author:   Sen Zhang
File:     test_skip.py
Version:  V1.0  2023/2/15 15:04
Describe: 
Steps:
    1.
    2.
    ...
"""
import unittest

version = 30

class TestSkip(unittest.TestCase):

    @unittest.skip("没原因")
    def test_1(self):
        print("方法1")

    @unittest.skipIf(version >= 30, "版本大于等于30，不测")
    def test_2(self):
        print("方法2")

    def test_3(self):
        print("方法3")