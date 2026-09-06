"""
这道题也能用数学方法解决：我们可以先把列表强制转换为集合（实现去重的操作），
然后分别计算列表中元素总和sum1以及集合中的元素总和sum2，二者相减从而得到出现两次的数字的总和sum3，
再用集合中元素的总和sum2减去sum3，得到的便是那个只出现一次的数字。

时间复杂度为O(n)（n为列表长度），空间复杂度为O(1)
"""

class Solution(object):
    def singleNumber(self, nums):
        nums_set = set(nums) # 把列表强制转换为集合（实现去重的操作）
        sum1 = sum(nums) # 计算列表中元素总和sum1
        sum2 = sum(nums_set) # 计算集合中的元素总和sum2
        sum3 = sum1 - sum2 # 出现两次的数字的总和sum3
        return sum2 - sum3 # 得到那个只出现一次的数字