"""
可变参数函数定义


Version: 0.1
Author: jacket-mouse
Date: 2024-05-09
"""

def add(*a):
    return sum(a)

print(add(1, 2, 3, 4, 5))