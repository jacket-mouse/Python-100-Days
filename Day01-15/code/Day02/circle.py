"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""
import math

r = float(input("请输入圆的半径："))
print("圆的周长和面积分别为： %.2f %.2f" % ((2 * math.pi * r), math.pi * (r ** 2)))

# anwser

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
