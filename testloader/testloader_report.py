# _*_ coding: utf-8 _*_
"""
Time:     2023/2/15 15:35
Author:   Sen Zhang
File:     testloader_report.py
Version:  V1.0  2023/2/15 15:35
Describe: 
Steps:
    1.
    2.
    ...
"""
import unittest
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover('../testcase', 'test_parameter_json.py')
with open("../reports/Html_Report2.html", "wb", ) as f:
    runner = HTMLTestRunner(f, 2, "HtmlTestRunner_测试报告", "python3.7")

    runner.run(suite)