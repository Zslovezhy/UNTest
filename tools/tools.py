# _*_ coding: utf-8 _*_
"""
Time:     2023/2/10 14:12
Author:   Sen Zhang
File:     tools.py
Version:  V1.0  2023/2/10 14:12
Describe: 
Steps:
    1.
    2.
    ...
"""
def add(a,b):
    return a + b

def login(username, password):
    if username == 'admin' and password == '123456':
        return '登录成功'
    else:
        return '登录失败'