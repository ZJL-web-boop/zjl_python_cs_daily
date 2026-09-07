"""
由于题目说只要有一个数在列表中出现了两次及以上，就返回True,否则返回False。
其实这是一道典型的消去重复数字的问题,如果去重之后数字的个数与去重之前相等，则意味着没有重复的数字。
所以我们这道题采用求长度方法去解决。

时间复杂度为O(n)（n为列表长度），空间复杂度为O(n)
"""


class Solution(object):
    def containsDuplicate(self, nums):
        nums_set = set(nums) # 把列表强制转换为集合（实现去重的操作），注意这里增加了空间复杂度
        return len(nums) !=len(nums_set) # 只要有一个数在列表中出现了两次及以上，意味着这二个长度就不相等，返回True,否则返回False。