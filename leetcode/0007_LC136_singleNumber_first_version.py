"""
由于题目说非空数组中除了一个数字只出现了一次，其余数字都出现了两次，
显然这是想提示我们用按位异或来解决这一问题。

时间复杂度为O(n)（n为列表长度），空间复杂度为O(1)
"""

class Solution(object):
    def singleNumber(self, nums):
        xor = 0 # 由于 0 ^ x = x ，所以这里的0对后续的异或操作没啥影响
        for i in nums:
            xor ^= i
        return xor