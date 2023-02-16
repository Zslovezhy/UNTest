# _*_ coding: utf-8 _*_
"""
Time:     2023/2/15 10:16
Author:   Sen Zhang
File:     test_assert.py
Version:  V1.0  2023/2/15 10:16
Describe: 
Steps:
    1.
    2.
    ...
"""
import unittest
from tools.tools import login

class TestLogin(unittest.TestCase):

    def test_login1(self):
        self.assertEqual('登录成功', login('admin', '123456'))

    def test_login2(self):
        self.assertEqual('登录成功', login('root', '123456'))

    def test_login3(self):
        self.assertEqual('登录失败', login('admin', '123123'))

    def test_login4(self):
        self.assertEqual('登录失败', login('aaa', '123456'))
        self.assertIn('失败', login('aaa', '123456'))