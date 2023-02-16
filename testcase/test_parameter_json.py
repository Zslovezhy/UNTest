# _*_ coding: utf-8 _*_
"""
Time:     2023/2/15 14:46
Author:   Sen Zhang
File:     test_parameter_json.py
Version:  V1.0  2023/2/15 14:46
Describe: 
Steps:
    1.
    2.
    ...
"""
import json
import unittest
from parameterized import parameterized
from tools.tools import login

def get_data():
    with open('../Data/data.json', encoding='utf-8') as f:
        result = json.load(f)
        data = []
        for i in result:
            data.append((i.get('username'), i.get('password'), i.get('except')))
    return data

class TestParameter(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_login(self, username, password, expect):
        self.assertEqual(expect, login(username, password))
