# _*_ coding: utf-8 _*_
"""
Time:     2023/2/15 16:13
Author:   Sen Zhang
File:     testloader_report_CN.py
Version:  V1.0  2023/2/15 16:13
Describe: 
Steps:
    1.
    2.
    ...
"""
import unittest
from HTMLTestRunner import HTMLTestRunner

unittest.TestLoader().discover('../testcase', 'test_parameter_json.py')