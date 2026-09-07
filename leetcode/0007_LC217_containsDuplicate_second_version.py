"""
第二版是在第一版的基础上加以优化的，优化点在于：第一版是直接通过把列表强制转换为集合来去重的，这是需要遍历列表中的所有元素的，
但是我们如果在遍历的过程中就已经发现有重复数字了，我们可以直接返回True，这样我们发现一对重复，立刻返回，剩下的数不用看，
平均效率更高。

时间复杂度与空间复杂度：
最好情况（重复就在开头）：均为O(1) -- 这是第一版做不到的地方
最坏情况（重复在最后面）：均为O(n)，与第一版一样
"""

class Solution(object):
    def containsDuplicate(self, nums):
        nums_set = set() # 定义一个空集合
        for i in nums:
            if i in nums_set: # 发现一对重复，立刻返回True，剩下的不用看；另外这是哈希集合，查询操作复杂度为O(1)
                return True
            nums_set.add(i)
        return False
