# _*_ coding: utf-8 _*_
"""
Time:     2023/2/9 17:55
Author:   Sen Zhang
File:     suite_runner.py
Version:  V1.0  2023/2/9 17:55
Describe: 学习TestSuite和TestRunner的使用
"""
# 导包
import unittest
from testcase01 import TestDemo1
from testcase02 import TestDemo2
from testcase03 import TestDemo3
# 实例化（创建对象）套件对象
suite = unittest.TestSuite()
# 使用套件对象添加用例方法
#方式1-1：suite.addTest(测试类名('方法名'))
# suite.addTest(TestDemo1('test_method1'))
# suite.addTest(TestDemo2('test_method1'))
# suite.addTest(TestDemo2('test_method2'))
# suite.addTest(TestDemo3('test_method1'))
#方式1-2：将一个测试类的所有方法进行添加
suite.addTest(unittest.makeSuite(TestDemo1))
suite.addTest(unittest.makeSuite(TestDemo2))
# 实例化运行对象
runner = unittest.TextTestRunner()
# 使用运行对象去执行套件对象
runner.run(suite)