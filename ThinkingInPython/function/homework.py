# -*- coding=utf-8 -*-
import math

a = float(input('请输入a的值：'))
b = float(input('请输入b的值：'))
c = float(input('请输入c的值：'))

def quadratic(a, b, c):
    # 求出判别式，根据判别式计算方程有几个解
    flag = pow(b, 2) - 4 * a * c
    # 1、当flag大于0时，表示方程有两个不相等的实数根
    if(flag > 0):
        x1 = (-b + math.sqrt(flag)) / 2*a
        x2 = (-b - math.sqrt(flag)) / 2*a
        return x1,x2
    # 2、当flag等于0时，表示方程有两个相等的实数根
    elif(flag == 0):
        x = -b / 2*a
        return x
    # 3、当flag小于0时，表示方程无实数根，但有两个共轭复根
    else:
        return '方程无实数解' 

print(quadratic(a, b, c))
