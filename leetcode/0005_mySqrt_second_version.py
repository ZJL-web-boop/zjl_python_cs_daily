""" 第二版：我们假设不能使用python内置函数pow或运算x**0.5，
我们应该采取的算法（一）如下
"""

# 此算法的时间复杂度为O(√x)，效率还是比较低的

class Solution(object):
    def mySqrt(self, x): # 题目要求：求非负整数的算术平方根（结果只保留整数部分，小数部分被截断）
        i = 0
        while i <= x: # 暴力遍历方法
            if i * i <= x < (i + 1) * (i + 1): # 注意这个判断条件，我们实际上是要不大于x的算术平方根的最大整数
                break
            i += 1
        return i
