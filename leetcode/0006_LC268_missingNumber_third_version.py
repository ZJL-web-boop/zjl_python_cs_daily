"""
第三版使用了数学方法解决这一问题：既然只少了[0,n]区间内的一个数，
那么我们就能够用这一区间的数的总和-列表中元素总和得到缺失的元素
算法的时间复杂度为O(n)，空间复杂度为O(1)
"""

class Solution(object):
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)