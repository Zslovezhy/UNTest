# _*_ coding: utf-8 _*_
"""
Time:     2023/2/10 14:43
Author:   Sen Zhang
File:     test_login.py
Version:  V1.0  2023/2/10 14:43
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
        if login('admin', '123456') == '登录成功':
            print('Pass')
        else:
            print('Fail')

    def test_login2(self):
        if login('root', '123456') == '登录成功':
            print('Pass')
        else:
            print('Fail')

    def test_login3(self):
        if login('admin', '123123') == '登录成功':
            print('Pass')
        else:
            print('Fail')

    def test_login4(self):
        if login('aaa', '123456') == '登录成功':
            print('Pass')
        else:
            print('Fail')


