# _*_ coding: utf-8 _*_
"""
Time:     2023/2/10 15:51
Author:   Sen Zhang
File:     test_fix.py
Version:  V1.0  2023/2/10 15:51
Describe: 
Steps:
    1.
    2.
    ...
"""
import unittest

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("------打开浏览器------")

    @classmethod
    def tearDownClass(cls) -> None:
        print("------关闭浏览器------")

    def setUp(self) -> None:
        print("输入网址......")

    def tearDown(self) -> None:
        print("关闭页面......")

    def test_1(self):
        print("1.输入用户名密码，点击登录")

    def test_2(self):
        print("2.输入用户名密码，点击登录")

    def test_3(self):
        print("3.输入用户名密码，点击登录")