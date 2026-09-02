class Solution(object):
    def mySqrt(self, x): # 题目要求：求非负整数的算术平方根（结果只保留整数部分，小数部分被截断）
        return int(pow(x,0.5)) # python的内置函数pow(x,i):求x的i次方，注意要int强制类型转换