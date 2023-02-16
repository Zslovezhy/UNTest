# _*_ coding: utf-8 _*_
"""
Time:     2023/2/9 17:54
Author:   Sen Zhang
File:     testcase02.py
Version:  V1.0  2023/2/9 17:54
Describe: 
Steps:
    1.
    2.
    ...
"""
import unittest

#2.自定义测试类
class TestDemo2(unittest.TestCase):
    #3.书写测试方法
    #必须以test_开头

    def test_method1(self):
        print("测试方法2-1")

    def test_method2(self):
        print("测试方法2-2")
        assert 3 > 2

#4.执行用例