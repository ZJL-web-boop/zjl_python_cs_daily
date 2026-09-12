class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2)) # 使用集合去重和集合的交集运算