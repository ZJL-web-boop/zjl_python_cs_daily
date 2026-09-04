"""
第一版：其实如果不在乎效率的话，解决这问题很容易
我们可以直接暴力遍历[0,n]里的数，看看哪个数不在数组里（时间复杂度为O(n²)）（n为数组长度）
空间复杂度为O(1)
"""

class Solution(object):
    def missingNumber(self,nums):
        length = len(nums) # 记录整数数组长度
        ans = 0 # 用来存放最后的答案
        for i in range(length+1): # 遍历[0,length]中的数，看看哪个数不在nums里
            if i not in nums: # 对nums从左到右进行遍历寻找是否有等于i的数，结果是没找到，单单这一层的复杂度为O(n)
                ans = i
                break
        return ans