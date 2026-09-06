"""
由于题目说只要有一个数在列表中出现了两次及以上，就返回True,否则返回False。
其实这是一道典型的消去重复数字的问题,如果去重之后的数字之和与去重之前相等，则意味着没有重复的数字。
所以我们这道题采用数学方法去解决。


"""


class Solution(object):
    def containsDuplicate(self, nums):
