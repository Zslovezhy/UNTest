# _*_ coding: utf-8 _*_
"""
Time:     2023/2/9 16:40
Author:   Sen Zhang
File:     01_testcase1.py
Version:  V1.0  2023/2/9 16:40
Describe: 书写方法
"""
import unittest

#2.自定义测试类
class TestDemo1(unittest.TestCase):
    #3.书写测试方法
    #必须以test_开头

    def test_method1(self):
        print("测试方法1-1")

    def test_method2(self):
        print("测试方法1-2")
        assert 3 > 2

#4.执行用例