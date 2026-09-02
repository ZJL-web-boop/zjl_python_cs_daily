""" 第三版：第二版暴力遍历的时间复杂度还是太大了，
所以我们这里采用效率较高的二分法解决这一问题
"""

# 二分算法本质上是利用了树这种数据结构，时间复杂度为O(log₂(x))。当x比较大时，使用此算法解决问题效率大幅提升

class Solution(object):
    def mySqrt(self,x): # 题目要求：求非负整数的算术平方根（结果只保留整数部分，小数部分被截断）
        left = 0 # 定义区间的左边界，从0开始往大走
        right = x # 定义区间的右边界，从x开始往小走
        ans = 0 # ans这个临时变量用来存放最终的答案，其初始值没有什么具体的含义
        while left <= right:
            mid = left + (right - left) // 2 # 每次都用区间中点的值去计算和比较
            if mid * mid <= x < (mid + 1) * (mid+1):
                ans = mid
                break
            elif mid * mid > x: # 目标值在mid的左边，则更新区间的右边界
                right = mid - 1
            else: # 目标值在mid的右边，则更新区间的左边界
                left = mid + 1
        return ans