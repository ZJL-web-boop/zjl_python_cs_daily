"""
由于题目说非空数组中除了一个数字只出现了一次，其余数字都出现了两次，
显然这是想提示我们用按位异或来解决这一问题。
"""

class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for i in nums:
            xor ^= i
        return xor