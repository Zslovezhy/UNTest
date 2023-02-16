# _*_ coding: utf-8 _*_
"""
Time:     2023/2/15 10:44
Author:   Sen Zhang
File:     test_parameter.py
Version:  V1.0  2023/2/15 10:44
Describe: 
Steps:
    1.
    2.
    ...
"""
import unittest
from parameterized import parameterized
from tools.tools import login

data = [
    ('admin', '123456', '登录成功'),
    ('root', '123456', '登录失败'),
    ('admin', '123123', '登录失败'),
    ('aaa', '123456', '登录失败')
]

class TestParameter(unittest.TestCase):

    @parameterized.expand(data)
    def test_login(self, username, password, expect):
        self.assertEqual(expect, login(username, password))



























