# _*_ coding: utf-8 _*_
"""
Time:     2023/2/10 15:02
Author:   Sen Zhang
File:     testloader1.py
Version:  V1.0  2023/2/10 15:02
Describe: 
Steps:
    1.
    2.
    ...
"""
import unittest

'''
1.实例化测试加载对象并添加用例   --->  得到的是suite对象
2.实例化运行对象
3.运行对象执行套件对象
'''
#unittest.TestLoader().discover('用例所在路径','用例代码文件名')
#用例代码文件名可以使用*通配符
suite = unittest.TestLoader().discover('../testcase', 'test*.py')
runner = unittest.TextTestRunner()
runner.run(suite)
