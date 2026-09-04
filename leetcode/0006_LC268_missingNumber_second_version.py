"""
第二版是在第一版的基础上进行优化，第一版的时间复杂度之所以为O(n²),是因为在循环里面又有一个in操作符：
如果针对列表进行查询的话，是要逐个遍历的，时间复杂度为O(n)。
那么我们能否使这个查询操作复杂度变为O(1)呢？ 使用哈希集合（set）（set不同于字典，它里面只有key，没有value）,查询时间复杂度为O(1)

但是由于引进了集合，空间复杂度为O(n)
"""

class Solution(object):
    def missingNumber(self, nums):
        nums_set = set(nums)  # 将列表转换为集合
        ans = 0 # 用来存放最后的答案
        for i in range(len(nums)+1): # 遍历[0,length]中的数，看看哪个数不在nums里
            if i not in nums_set: # 此步的时间复杂度为O(1)
                ans = i
                break
        return ans